from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<str:slug>/", views.product_detail, name="product-detail"),
    path("add_to_cart/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("delete_cart_item/", views.delete_cart_item, name="delete_cart_item"),
    path("create_order/", views.create_order, name="create_order"),
    path("checkout/<order_id>/", views.checkout, name="checkout"),
    path("coupon_apply/<order_id>/", views.coupon_apply, name="coupon_apply"),
    path("payment_status/<order_id>/", views.payment_status, name="payment_status"),
    path("paypal_payment_verify/<order_id>/", views.paypal_payment_verify, name="paypal_payment_verify"),
    path("stripe_payment/<order_id>/", views.stripe_payment, name="stripe_payment"),
    path("stripe_payment_verify/<order_id>/", views.stripe_payment_verify, name="stripe_payment_verify"),
    path("paystack_payment_verify/<order_id>/", views.paystack_payment_verify, name="paystack_payment_verify"),
    
]
