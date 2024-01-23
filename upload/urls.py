from django.urls import path, re_path

from rest_framework.routers import DefaultRouter
from .views import redirect_to_random, handle_file_upload, delete_upload


app_name = 'upload'

urlpatterns = [
    path('', redirect_to_random, name='upload'),
    path('<str:random_str>/', handle_file_upload),
    path('<str:random_str>/delete/<int:file_id>/', delete_upload),
]

