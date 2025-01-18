import Swal from "./node_modules/sweetalert2/src/sweetalert2.js";

$(document).ready(function() {
    const Toast = Swal.mixin({
        toast : true,
        position: "top",
        showConfirmationButton: false,
        timer: 2000,
        timerProgressBar: true,
    });
    function generateCartId() {
        const ls_cartid = localStorage.getItem("cartId");

        if (ls_cartid === null) {
            var cartId = "";

            for (var i = 0; i < 10; i++) {
                cartId += Math.floor(Math.random() * 10);
            }

            localStorage.setItem("cartId", cartId);
        }
        return ls_cartid || cartId;
    }
    

    $(document).on('click', '.add_to_cart', function(){
        const button_el = $(this);
        const id = button_el.attr("data-id");
        const qty = $(".quantity").val();
        const size = $("input[name='size']:checked").val();
        const color = $("input[name='color']:checked").val();
        const cart_id = generateCartId();

        $.ajax({
            url: "/add_to_cart/",
            data : {
                id:id,
                qty: qty,
                size: size,
                color: color,
                cart_id: cart_id,
            },
            beforeSend: function () {
                button_el.html("Adding to Cart <i class='fas fa-spinner fa-spin ms-2'></i>");
            },
            success: function(response){
                console.log(response)
                Toast.fire({
                    icon: "success",
                    title: response?.message,
                });
                button_el.html("Add to Cart <i class='fas fa-shopping-cart ms-2'></i>");
                $(".total_cart_items").text(response?.total_cart_items);

            },
            error: function(xhr, status, error){
                console.log("Error Status: ", xhr.status);
                console.log("Response Text: ", xhr.responseText);
                let errorResponse = JSON.parse(xhr.responseText);

                Toast.fire({
                    icon: "success",
                    title: errorResponse?.error,
                });
            }
        });

    });

    //update cart quantity
    $(document).on('click', '.update_cart_qty', function(){
        const button_el = $(this);
        const update_type = button_el.attr('data-update-type');
        const item_id = button_el.attr('data-item-id');
        let qty = parseInt($(".item-qty-" + item_id).val());
        const product_id = button_el.attr('data-product-id');
        const cart_id = generateCartId();
        const stock = parseInt($(".item-qty-" + item_id).attr('data-qty')); // Get stock from data attribute
    
        if (update_type === "increase") {
            if (qty < stock) {
                $(".item-qty-" + item_id).val(qty + 1);
                qty++;
            } else {
                // button_el.html("+"); // Reset button text if exceeding stock
                return; // Stop further execution if quantity exceeds stock
            }
        } else {
            if (qty > 1) {
                $(".item-qty-" + item_id).val(qty - 1);
                qty--;
                // button_el.html("-"); // Reset button text if exceeding stock
            } else {
                $(".item-qty-" + item_id).val(1);
                qty = 1;
            }
        }
    
        // Proceed with the AJAX call if the quantity is within stock limits
        $.ajax({
            url: "/add_to_cart/",
            data: {
                id: product_id,
                qty: qty,
                cart_id: cart_id,
            },
            beforeSend: function () {
                button_el.html("<i class='fas fa-spinner fa-spin ms-2'></i>");
            },
            success: function(response) {
                console.log(response);
                Toast.fire({
                    icon: "success",
                    title: response?.message,
                });
                $(".item_sub_total_" + item_id).text(response.item_sub_total);
                $(".cart_sub_total").text(response.cart_sub_total);
                if (update_type === "increase") {
                    button_el.html("<i class='fa fa-plus'></i>");
                } else {
                    button_el.html("<i class='fa fa-minus'></i>");
                }
            },
            error: function(xhr, status, error) {
                console.log("Error Status: ", xhr.status);
                console.log("Response Text: ", xhr.responseText);
                let errorResponse = JSON.parse(xhr.responseText);
                Toast.fire({
                    icon: "error",
                    title: errorResponse?.error,
                });
                // Reset quantity input and button text on error
                $(".item-qty-" + item_id).val(stock); // Set input value to stock limit
                if (update_type === "increase") {
                    button_el.html("<i class='fa fa-plus'></i>");
                } else {
                    button_el.html("<i class='fa fa-minus'></i>");
                }
            }
        });
    });
    
    
    

    //delete item from cart
    $(document).on('click', '.delete_cart_item', function(){
        const button_el = $(this);
        const item_id = button_el.attr('data-item-id');
        const product_id = button_el.attr('data-product-id');
        const cart_id = generateCartId();

        $.ajax({
            url: "/delete_cart_item/",
            data: {
                id: product_id,
                item_id: item_id,
                cart_id: cart_id,
            },
            beforeSend: function () {
                button_el.html("<i class='fas fa-spinner fa-spin ms-2'></i>");
            },
            success: function(response){
                console.log(response)
                Toast.fire({
                    icon: "success",
                    title: response?.message,
                });
                $(".total_cart_items").text(response?.total_cart_items);
                $(".cart_sub_total").text(response?.cart_sub_total);
                $(".item_div_" + item_id).addClass("d-none");

            },
        });
    });
});





  