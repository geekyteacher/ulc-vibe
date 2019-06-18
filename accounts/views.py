#from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect, HttpResponse


# accounts/views.py
class sign_up(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html' 

def accounts_index(request):
    context = {
        "activate":"accounts",
    }
    return render(request, 'accounts_index.html',context)
