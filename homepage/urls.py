from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, CategoryViewSet, ItemViewSet, DownloadViewSet


app_name = 'homepage'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)
router.register(r'downloads', DownloadViewSet)


urlpatterns = [  
    # 主页  
    path('', index, name='index'),
    path('api/', include(router.urls)),
]


