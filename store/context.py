from store import models as store_models

def default(request):
    try:
        cart_id = request.session['cart_id']
        total_cart_items = store_models.Cart.objects.filter(cart_id=cart_id)
    except:
        total_cart_items = []
    return{
        "total_cart_items":len(total_cart_items)
    }
