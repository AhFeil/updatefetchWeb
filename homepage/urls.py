from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, redirect_to_download, CategoryViewSet, ItemViewSet, DownloadViewSet


app_name = 'homepage'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'downloads', DownloadViewSet)


urlpatterns = [  
    # 主页  
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('<str:app_name>-<str:system>-<str:architecture>/', redirect_to_download, name='redirect_to_download'),
]


