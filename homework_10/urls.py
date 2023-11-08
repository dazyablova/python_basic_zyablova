from django.urls import path
from .views import category_list, product_list
from django.urls import path
from .views import CategoryListView, ProductDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', product_list, name='product_list'),
]