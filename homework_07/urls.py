from django.urls import path
from .views import category_list, product_list

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', product_list, name='product_list'),
]