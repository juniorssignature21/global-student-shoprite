from django.contrib import admin
from . import models as storeModels

# Register your models here.

class GalleryInline(admin.TabularInline):
    model = storeModels.Gallery
    
class VariantInline(admin.TabularInline):
    model = storeModels.Variant
    
class VariantItemInline(admin.TabularInline):
    model = storeModels.VariantItem
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]
    list_editable = ["image"]
    prepopulated_fields = {"slug": ('title',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "regular_price", "stock", "status", "featured", "vendor", "date"]
    search_fields = ["name", "category__title"]
    list_filter = ["status", "featured", "category"]
    inlines = [GalleryInline, VariantInline]
    prepopulated_fields = {"slug": ('name',)}
    
class VariantAdmin(admin.ModelAdmin):
    list_display = ["product", "name"]
    search_fields = ["product__name", "name"]
    inlines = [VariantItemInline]
    
    
class VariantItemAdmin(admin.ModelAdmin):
    list_display = ["variant", "title", "content"]
    search_fields = ["variant__name", "title"]
    # inlines = [VariantInline]
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["product", "name"]
    search_fields = ["product__name", "gallery__id"]
    
    
class CartAdmin(admin.ModelAdmin):
    list_display = ["cart_id", "product", "user", "qty", "price" , "total", "date"]
    search_fields = ["cart_id", "product__name", "user__username"]
    list_filter = ["date", "product"]
    
class CouponAdmin(admin.ModelAdmin):
    list_display = ["code", "vendor", "discount"]
    search_fields = ["code", "vendor__username"]
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "customer", "total", "payment_status", "order_status", "payment_method"]
    list_editable = ["payment_status", "order_status", "payment_method"]
    search_fields = ["order_id", "customer__username"]
    list_filter = ["payment_status", "order_status"]
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["item_id", "order", "product", "qty", "price", "total"]
    search_fields = ["item_id", "order__order_id", "product__name"]
    list_filter = ["order__date"]
    
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rating", "active", "date"]
    search_fields = ["user__username", "product__name"]
    list_filter = ["active", "rating"]
    
    
    
admin.site.register(storeModels.Product, ProductAdmin)
admin.site.register(storeModels.Variant, VariantAdmin)
admin.site.register(storeModels.VariantItem, VariantItemAdmin)
admin.site.register(storeModels.Order, OrderAdmin)
admin.site.register(storeModels.OrderItem, OrderItemAdmin)
admin.site.register(storeModels.Coupon,CouponAdmin)
admin.site.register(storeModels.Cart,CartAdmin)
admin.site.register(storeModels.Category, CategoryAdmin)
admin.site.register(storeModels.Review, ReviewAdmin)
# admin.site.register