from django.shortcuts import render

def index(request):
    context = {
        "activate":"home",
    }
    return render(request, "index.html", context)