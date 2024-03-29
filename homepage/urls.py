from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

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
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/homepage/images/favicon.ico')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
