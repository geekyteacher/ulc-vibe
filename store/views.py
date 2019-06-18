from django.shortcuts import render
from store.models import Category, Product

# Create your views here.
def store_index(request):
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "activate":"categories",
    }
    return render(request, 'store_index.html',context)

def store_category(request, pk):
    
    products = Product.objects.all()
    x = Category.objects.get(pk=pk)
    categories = Category.objects.filter(
        parent_id__name__contains=x
    )
    context = {
        "category":x,
        "categories":categories,
        "activate":"store",
        "products":products,
    }
    return render(request, "store_category.html", context)