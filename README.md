# updatefetchWeb


在网页上展示 UpdateFetch 下载的内容，方便使用。

网址： [UpdateFetch Web](http://185.149.146.103:7699/)


## 思路

使用 Django，通过 API 接收 UpdateFetch 的信息，更新已下载的文件的元信息和最新版下载链接，在主页展示。


## 管理员


必须创建 local_settings.py 文件，并定义配置


```python
import os

DEBUG = False
# 添加自己的 ip 或域名，否则不能使用
ALLOWED_HOSTS = ['updatefetch.vfly2.com', 'localhost', '127.0.0.1']


# 如果使用网页暂存区，这段需要配置好，否则不用管
from upload.uploader import MinioUploader
upload_temporary_dir = "temp/"
up_app = "mc"
# 优先使用环境变量定义的值
minio_bucket_path = os.environ.get('MINIO_BUCKET_PATH', "your_minio_alias/upload")
minio_server = os.environ.get('MINIO_SERVER', "your_minio_ip:9000")
minio_uploader = MinioUploader(up_app, minio_bucket_path, minio_server)

# 默认图片和版本名
undefined_image_url = 'https://ib.ahfei.blog:443/imagesbed/undefined_image_url_200-24-01-05.webp'
undefined_version = 'undefined version'


LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'


STATIC_URL = 'static/'
STATIC_ROOT = '/home/hoo/static/updatefetch'
```




安装流程： **待写**



## 使用


配置好，正常运行之后

1. 到后台











## API

网页： http://ip:7699/api




## 网页暂存区

> 不完善，勉强能用

文件版的 webnote，方便上传文件，分享文件的。用以补充 UpdateFetch 不能下载的软件等。



