from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.accounts_index, name='account_index'),
    path('signup/', views.sign_up.as_view(), name='signup'),
]