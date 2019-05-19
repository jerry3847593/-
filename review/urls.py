from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('post/<int:post_id>/', views.detail, name = 'detail'),
    path('post/new/', views.post_new, name= 'new'),
    path('post/<int:post_id>/edit/',views.post_edit, name= 'edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name= 'delete'),
]