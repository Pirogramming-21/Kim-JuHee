# urls.py

from django.urls import path
from .views import *
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Ensure this pattern is included
    path('create', views.post_create, name='post_create'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    path('<int:pk>/update', views.post_update, name='post_update'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
    path('<int:post_id>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('<int:post_id>/update_interest/', views.update_interest, name='update_interest'),
]