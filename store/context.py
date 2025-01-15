from store import models as store_models

def default(request):
    try:
        cart_id = request.session['cart_id']
        total_cart_items = store_models.Cart.objects.filter(cart_id=cart_id)
    except KeyError:
        # Handle the case where 'cart_id' is not in session
        total_cart_items = []
    except store_models.Cart.DoesNotExist:
        # Handle the case where no cart items are found
        total_cart_items = []
    
    return {
        "total_cart_items": len(total_cart_items)
    }
