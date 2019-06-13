from django.shortcuts import render
from store.models import Category

# Create your views here.
def store_index(request):
    context = {
        "activate":"store",
    }
    return render(request, "store_index.html",context)

def store_categories(request):
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "activate":"categories",
    }
    return render(request, 'store_cats.html',context)