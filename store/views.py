from django.shortcuts import render

# Create your views here.
def store_index(request):
    context = {
        "activate":"store",
    }
    return render(request, "store_index.html",context)