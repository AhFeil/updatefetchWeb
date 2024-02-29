# updatefetchWeb


在网页上展示 UpdateFetch 下载的内容，方便使用。

可以前往演示网页体验： [UpdateFetch Web](http://185.149.146.103:7699/)


## 思路

使用 Django，通过 API 接收 UpdateFetch 的信息，更新已下载的文件的元信息和最新版下载链接，在主页展示。


## 管理员


必须创建 local_settings.py 文件，并定义配置


```python
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False
# 添加自己的 ip 或域名，否则不能使用
ALLOWED_HOSTS = ['updatefetch.vfly2.com', 'localhost', '127.0.0.1']

# 默认图片和版本名
undefined_image_url = 'https://ib.ahfei.blog:443/imagesbed/undefined_image_url_200-24-01-05.webp'
undefined_version = 'undefined version'

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


# 如果使用网页暂存区，这段需要配置好，否则不用管
from upload.uploader import MinioUploader
upload_temporary_dir = "temp/"
up_app = "mc"
# 优先使用环境变量定义的值
minio_bucket_path = os.environ.get('MINIO_BUCKET_PATH', "your_minio_alias/upload")
minio_server = os.environ.get('MINIO_SERVER', "your_minio_ip:9000")
minio_uploader = MinioUploader(up_app, minio_bucket_path, minio_server)
```

可以使用环境变量也可以在 local_settings.py 文件中直接写入

```
export MINIO_BUCKET_PATH="vrm/upload"
export MINIO_SERVER="88.214.22.106:9000"
```



安装流程： [updatefetchWeb 的安装步骤 - 技焉洲 (vfly2.com)](https://technique.vfly2.com/2024/03/deployment-process-of-updatefetchweb/)



## 使用


配置好，正常运行之后

到后台，访问 ip:7699/admin
1. **增加 Category**，Title 填入 `Uncategorized` 即可，在 UpdateFetch 下载项配置里，未指定分类时，会放在这里。
2. 增加 Category，手动创建其他的分类，比如 Server、Client，只有创建的分类才能在 UpdateFetch 下载项配置中使用。
3. **增加 Token**，否则 UpdateFetch 无权限上传信息，token 样式为 12719f3e356d96c47ed031645d411c23f4b219e1

然后在 UpdateFetch 的配置文件中，设置好 web 的 ip 和端口，以及 token 即可在下载后，更新 web 的信息


### 自动跳转到最新版的下载网址

为了方便在脚本中使用，还支持以一定格式获取最新版的下载链接。

比如要获取 xray 的 Windows 平台 AMD64 架构的文件，可以直接访问 http://ip:7699/xray-win-amd64 ，本程序会跳转到最新的网址

格式为： 软件名-系统-架构，软件名必须是第一个。系统和架构有别名，Windows 可以填 win 或 windows，具体查看 settings.py 中的设置。

配合 bash 脚本的示例：

```sh
url="185.149.146.103:7699/xray-linux-arm64"
# 获取最终的重定向URL
redirect_url=$(curl -Ls -o /dev/null -w %{url_effective} $url)
# 下载文件
curl -LO "$redirect_url"
```


## API

网页： http://ip:7699/api




## 网页暂存区

> 不完善，勉强能用

文件版的 webnote，方便上传文件，分享文件的。用以补充 UpdateFetch 不能下载的软件等。



