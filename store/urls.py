from django.urls import path, include
from . import views

urlpatterns = [
    path('store/', views.store_index, name="store_index"),
]