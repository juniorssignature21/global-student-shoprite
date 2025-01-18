function payWithPaystack() {
    // Initialize Paystack payment
    var handler = PaystackPop.setup({
        key: "{{paystack_public_key}}", // Replace with your public key
        email: "{{order.address.email}}", // Customer email
        amount:"{{amount_in_kobo}}", // Amount in kobo (multiply by 100)
        currency: "NGN", // Currency
        ref:"" + Math.floor(Math.random() * 1000000000 + 1), // Unique transaction reference from your API
        callback: function(response) {
            // Handle successful payment
            window.location.href = ('/paystack_payment_verify/{{order.order_id}}/?reference=' + response.reference + "&payment_methon=Paystack");
            // Optionally, verify payment by sending response.reference to your server
        },
        onClose: function() {
            alert('Transaction was not completed, window closed.');
        },
    });
    handler.openIframe(); // Open the payment modal
}