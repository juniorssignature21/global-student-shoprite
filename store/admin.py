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
    
    
    
admin.site.register(storeModels.Product)