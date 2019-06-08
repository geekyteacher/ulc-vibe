from django.contrib import admin
from store.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
