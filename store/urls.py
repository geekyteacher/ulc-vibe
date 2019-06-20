from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.store_index, name="store_index"),
    path('',views.store_index, name="store_index"),
    path('<pk>/',views.store_category, name="store_category"),
    path('<pk>/',views.store_subcategory, name="store_subcategory"),
]