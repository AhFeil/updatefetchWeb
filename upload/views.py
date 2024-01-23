from django.shortcuts import render

# Create your views here.
import os, random, string
from .models import Upload
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseNotFound

from updatefetchWeb.settings import upload_temporary_dir, minio_uploader


def generate_random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def redirect_to_random(request):
    random_str = generate_random_string()
    return redirect(f'/up/{random_str}/')


def handle_file_upload(request, random_str):
    if request.method == 'POST':
        file = request.FILES['file']
        filename = file.name
        file_path = upload_temporary_dir + filename
        
        fs = FileSystemStorage(location=upload_temporary_dir)
        fs.save(filename, file)
        # Upload to MinIO server
        try:
            minio_uploader.import_config(file_path, random_str)
            minio_uploader.run()
            links = minio_uploader.get_uploaded_files_link()
            link = links[0]
            # Save the object data in the database
            upload = Upload(
                path=random_str,
                file_name=os.path.splitext(filename)[0],
                suffix_name=os.path.splitext(filename)[1],
                link=link,
            )
            upload.save()
        except Exception as exc:
            print('Error occurred while uploading to MinIO:', exc)
            return HttpResponseNotFound('<h1>上传失败</h1>')
        # 上传完成后，删除本地文件
        os.remove(fs.path(filename))
        return redirect(f'/up/{random_str}/')
    
    uploads = Upload.objects.filter(path=random_str)
    return render(request, 'upload/upload.html', {'uploads': uploads, 'random_str': random_str})


def delete_upload(request, random_str, file_id):
    upload = Upload.objects.get(id=file_id, path=random_str)
    try:
        minio_uploader.delete(upload.path, upload.file_name + upload.suffix_name)
        upload.delete()
        return redirect(f'/up/{random_str}/')
    except Exception as exc:
        print('Error occurred while deleting from MinIO:', exc)
        return HttpResponseNotFound('<h1>删除失败</h1>')
