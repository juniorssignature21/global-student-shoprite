function initPayPalButton() {
    paypal.Buttons({
        style: {
            shape: "rect",
            color: "gold",
            layout: "vertical",
            label: "paypal",
        },
        createOrder: function (data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        currency_code: "USD",
                        value: "{{order.total}}", // Replace with dynamic order total
                    },
                }],
            });
        },
        onApprove: function (data, actions) {
            return actions.order.capture().then(function(orderData) {
                // Show a success message within this page
                const element = document.getElementById("paypal-button-container");
                element.innerHTML = "<h5>Verifying payment...</h5>";
                window.location.href = `/paypal_payment_verify/{{order.order_id}}/?transaction_id=${orderData.id}`;
            });
        },
        onError: function (err) {
            console.log(err);
        }
    }).render("#paypal-button-container");
}
document.addEventListener("DOMContentLoaded", function () {
    initPayPalButton();
});


