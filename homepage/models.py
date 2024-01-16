from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.title


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)   # 在前层，实现未定义则划分为 未分类 的类别中，因为这里不能保证类被创建
    name = models.CharField(max_length=50)
    image = models.URLField(blank=True, default='http://default_image_url_here')
    website = models.URLField(blank=True, default='http://undefined_website')
    version = models.CharField(max_length=50, blank=True, default='undefined version')

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.name


class Download(models.Model):
    item = models.ForeignKey(Item, related_name='downloads', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    # architecture = models.CharField(max_length=50)
    link = models.URLField()
