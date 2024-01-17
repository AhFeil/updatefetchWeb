from django.shortcuts import render

from .models import Category, Item, Download


def index(request):
    categories = Category.objects.all()
    return render(request, 'homepage/homepage.html', {'categories': categories})


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

