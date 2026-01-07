from django.urls import path
from .views import register_view , login_view , dashboard_view,logout_view,delete_note_view,edit_note_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('delete-note/<int:note_id>/', delete_note_view, name='delete_note'),
    path('edit-note/<int:note_id>/', edit_note_view, name='edit_note'),

]