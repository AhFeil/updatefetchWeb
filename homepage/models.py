from django.db import models
from updatefetchWeb.settings import undefined_image_url, undefined_version, PLATFORM_CHOICES, ARCHITECTURE_CHOICES


class Category(models.Model):
    """每个分类的一些元信息"""
    title = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.title


class Item(models.Model):
    """每个下载项的一些元信息"""
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)   # 在前层，实现未定义则划分为 未分类 的类别中，因为这里不能保证类被创建
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField(blank=True, default=undefined_image_url)
    website = models.URLField(blank=True)
    version = models.CharField(max_length=50, blank=True, default=undefined_version)

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.name


class Download(models.Model):
    """每个 item 在不同平台、不同架构下，对应着不同的下载链接"""
    item = models.ForeignKey(Item, related_name='downloads', on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default="windows")
    architecture = models.CharField(max_length=20, choices=ARCHITECTURE_CHOICES, default='amd64')
    link = models.URLField(unique=True)

    def __str__(self):
        """返回模型的字符串表示。"""
        return '-'.join([self.item.name, self.platform, self.architecture])
