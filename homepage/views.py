from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound

from .models import Category, Item, Download
from updatefetchWeb.settings import ALL_SYSTEM, ALL_ARCH, SYSTEM_LIST, ARCH_LIST, ALL_SYSTEM_ARCH

def index(request):
    categories = Category.objects.all()
    return render(request, 'homepage/homepage.html', {'categories': categories})


def redirect_to_download(request, app_name, system, architecture):
    """正确顺序应该是，名称-系统-架构"""
    print(f"{app_name}-{system}-{architecture}")
    # 根据名称获取 Item 对象，不存在直接返回 404
    item = get_object_or_404(Item, name=app_name)

    # 只有规定的字段才处理
    if not (system in ALL_SYSTEM_ARCH and architecture in ALL_SYSTEM_ARCH):
        return HttpResponseNotFound('<h1>请使用规定的字段</h1>')
    # 经过调整，系统和架构不会颠倒，
    if system in ALL_SYSTEM and architecture in ALL_ARCH:
        pass
    elif system in ALL_ARCH and architecture in ALL_SYSTEM:
        system, architecture = architecture, system
    else:   # 加入是 name-win-win 这种，也直接报错
        return HttpResponseNotFound('<h1>系统和架构处有问题</h1>')

    # 这样就都是标准的架构名和系统名了
    for specific_system in SYSTEM_LIST:
        if system in specific_system['alias']:
            system = specific_system['standard_name']
            break
    for specific_arch in ARCH_LIST:
        if architecture in specific_arch['alias']:
            architecture = specific_arch['standard_name']
            break
    
    print(f"{app_name}-{system}-{architecture}")
    # 获取与提供的系统和架构对应的 Download 对象
    download = get_object_or_404(Download, item=item, platform=system, architecture=architecture)

    # 重定向到实际的下载链接
    return redirect(download.link)


# API
from rest_framework import viewsets
from .serializers import CategorySerializer, ItemSerializer, DownloadSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DownloadViewSet(viewsets.ModelViewSet):
    queryset = Download.objects.all()
    serializer_class = DownloadSerializer

