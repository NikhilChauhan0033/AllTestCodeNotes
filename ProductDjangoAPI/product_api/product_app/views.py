from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Sum,Q
from .pagination import ProductPagination

class ProdcutListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.all()

        # is_active filter
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == "true")

        # min & max price filter
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(product_price__gte=min_price)

        if max_price:
            queryset = queryset.filter(product_price__lte=max_price)

        # search
        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(
                Q(product_name__icontains=search) |
                Q(product_description__icontains=search)
            )

        # date filter
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date:
            queryset = queryset.filter(created_at__date__gte=start_date)

        if end_date:
            queryset = queryset.filter(created_at__date__lte=end_date)

        return queryset
    

class ProductRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAggregationAPI(APIView):
    def get(self, request):
        active_sum = Product.objects.filter(is_active=True).aggregate(
            total=Sum('product_price')
        )['total']

        inactive_sum = Product.objects.filter(is_active=False).aggregate(
            total=Sum('product_price')
        )['total']

        return Response({
            "active_total_price": active_sum or 0,
            "inactive_total_price": inactive_sum or 0
        })
    
