from django.urls import path
from .views import ProductList, ProductCategory, product_detail, SearchResultsView

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<category_name>', ProductCategory.as_view()),
    path('product/<id>', product_detail, name='productdetail'),
    path('products/search/', SearchResultsView.as_view(), name='search_results'),


]