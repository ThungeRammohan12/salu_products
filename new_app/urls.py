from django.urls import path
from .views import add_salu_product, search_salu_products

urlpatterns = [
    path('add/', add_salu_product),
    path('search/', search_salu_products),
]
