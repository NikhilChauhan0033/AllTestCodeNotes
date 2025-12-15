from django.urls import path
from .views import ProductView,ProductUpdateDestroyView
from myapp import views

urlpatterns = [
    path('api/products/',ProductView.as_view(),name='api/products/'),
    path('api/products/<int:pk>/',ProductUpdateDestroyView.as_view(),name='api/productsupdatedestroy/'),

    path('',views.index ,name='index'),
    path('delete/<int:id>/',views.delete_view,name='delete_view'),
    path('update/<int:id>/',views.update_view,name='update_view')
]