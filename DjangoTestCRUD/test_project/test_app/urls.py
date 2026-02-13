from django.urls import path
from test_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:id>/',views.delete_record,name='delete'),
    path('edit/<int:id>/',views.edit_record,name='edit')
]