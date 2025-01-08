from django.shortcuts import render
from django.http import JsonResponse
from store import models as store_models
from django.contrib import messages
from django.db.models import Q, Avg, Sum
from decimal import Decimal

# Create your views here.

def index(request):
    products = store_models.Product.objects.filter(status="Published")
    context = {
        "products":products,
    }
    return render(request, "store/index.html", context)

def product_detail(request, slug):
    products = store_models.Product.objects.get(status="Published", slug=slug)
    related_product = store_models.Product.objects.filter(category=products.category, status="Published").exclude(id=products.id)
    
    product_stock_range = range(1, products.stock + 1)
    
    
    context = {
        "products": products,
        "related_product": related_product,
        "product_stock_range": product_stock_range,
    }
    
    return render(request, "store/detail.html", context)

def add_to_cart(request):
    id =  request.GET.get("id")
    qty = request.GET.get("qty")
    color = request.GET.get("color")
    size = request.GET.get("size")
    cart_id = request.GET.get("cart_id")
    
    request.session["cart_id"] = cart_id
    
    if not id or not qty or not cart_id:
        return JsonResponse({"error": "No id, qty or cart_id"}, status=400)
    try:
        products = store_models.Product.objects.get(status="Published", id=id)
    except store_models.Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    
    existing_cart_items = store_models.Cart.objects.filter(cart_id=cart_id, product=products).first()
    if int(qty) > products.stock:
        return JsonResponse({"error": "Quantity exceed current stock amount"}, status=404)
    
    if not existing_cart_items:
        cart = store_models.Cart()
        cart.product = products    
        cart.price = products.price    
        cart.color = color     
        cart.size=  size
        cart.sub_total = Decimal(products.price) * Decimal(qty)
        cart.shipping = Decimal(products.shipping) * Decimal(qty)
        cart.total = cart.sub_total + cart.shipping
        cart.user = request.user if request.user.is_authenticated else None
        cart.cart_id = cart_id
        cart.save()
        
        message = "Item added to cart"
        
    else:
        existing_cart_items.product = products    
        existing_cart_items.price = products.price    
        existing_cart_items.color = color     
        existing_cart_items.size=  size
        existing_cart_items.sub_total = Decimal(products.price) * Decimal(qty)
        existing_cart_items.shipping = Decimal(products.shipping) * Decimal(qty)
        existing_cart_items.total = existing_cart_items.sub_total + existing_cart_items.shipping
        existing_cart_items.user = request.user if request.user.is_authenticated else None
        existing_cart_items.cart_id = cart_id
        existing_cart_items.save()
        
        message = "Cart updated"
    
    total_cart_items = store_models.Cart.objects.filter(Q(cart_id=cart_id) | Q(cart_id=cart_id))
    cart_sub_total = store_models.Cart.objects.filter(Q(cart_id=cart_id) | Q(cart_id=cart_id)).aaggregate(sub_total=Sum("sub_toal"))["sub_total"]
    return JsonResponse(
        {
            "message": message,
            "total_cart_items":total_cart_items.count(),
            "cart_sub_total": "{:,.2f}".format(cart_sub_total),
            "items_sub_total": "{:,.2f}".format(existing_cart_items.sub_total) if existing_cart_items else "{:,.2f}".format(cart.cart_sub_total)
        })        
            
    
    