from django.urls import path
from .views import ProdcutListCreateAPI,ProductAggregationAPI

urlpatterns = [
    path('api/products/',ProdcutListCreateAPI.as_view(),name='product'),
    path('api/products/aggregate/', ProductAggregationAPI.as_view())

]