from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.store_index, name="store_index"),
    path('',views.store_categories, name="store_categories"),
]