from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('create/', post_create, name='post_create'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('<int:pk>/update/', post_update, name='post_update'),
    path('<int:pk>/delete/', post_delete, name='post_delete'),
    path('<int:pk>/comment/create/', comment_create, name='comment_create'),
    path('<int:post_pk>/comment/<int:comment_pk>/delete/', comment_delete, name='comment_delete'),
    path('like_ajax/', like_ajax, name='like_ajax'),
]
