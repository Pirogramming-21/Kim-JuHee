from django.urls import path
from .views import *

app_name='posts'

urlpatterns = [
    path('', post_list),
    path('create', post_create),
    path('<int:pk>', post_detail),
    path('<int:pk>/update', post_update),
    path('<int:pk>/delete', post_delete),
]