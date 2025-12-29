from django.urls import path
from .views import ProdcutListCreateAPI,ProductAggregationAPI,ProductRetrieveUpdateDestroyAPI

urlpatterns = [
    path('api/products/',ProdcutListCreateAPI.as_view(),name='product'),
    path('api/products/<int:pk>/',ProductRetrieveUpdateDestroyAPI.as_view()),
    path('api/products/aggregate/', ProductAggregationAPI.as_view())

]