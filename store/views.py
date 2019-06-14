from django.shortcuts import render
from store.models import Category

# Create your views here.
def store_index(request):
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "activate":"categories",
    }
    return render(request, 'store_index.html',context)

def store_category(request, pk):
    x = Category.objects.get(pk=pk)
    categories = Category.objects.filter(
        parent_id__name__contains=x
    )
    context = {
        "category":x,
        "categories":categories,
        "activate":"store",
    }
    return render(request, "store_category.html", context)