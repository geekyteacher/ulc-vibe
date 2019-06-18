from django.contrib import admin
from store.models import Category, Product, ProductPicture, Size

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")

class ProductPictureInline(admin.TabularInline):
    model = ProductPicture

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductPictureInline,
    ]

class SizeAdmin(admin.ModelAdmin):
    list_display = ("name","description")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)