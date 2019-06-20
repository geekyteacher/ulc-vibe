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
    #catName = Category.objects.get(name=name)
    catID = Category.objects.get(pk=pk)
    categories = Category.objects.filter(
        parent_id__name__contains=catID
    )
    context = {
        #"catName":catName,
        "category":catID,
        "categories":categories,
        "activate":"store",
        "products":products,
    }
    return render(request, "store_category.html", context)

def store_subcategory(request, parent_pk, pk):
    
    products = Product.objects.all()
    
    catID = Category.objects.get(pk=pk)
    categories = Category.objects.filter(
        parent_id__name__contains=catID
    )
    context = {
        "category":catID,
        "categories":categories,
        "activate":"store",
        "products":products,
    }
    return render(request, "store_subcategory.html", context)

def store_product(request, item):
    item = Product.objects.all()
    return render(request, "store_product.html", context)