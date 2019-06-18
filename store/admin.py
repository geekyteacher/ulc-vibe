from django.contrib import admin
from store.models import Category, Product, ProductPicture

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")

class ProductPictureInline(admin.TabularInline):
    model = ProductPicture
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "stock")
    inlines = [
        ProductPictureInline,
    ]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
