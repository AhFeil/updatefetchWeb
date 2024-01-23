import subprocess
import os
from abc import ABC, abstractmethod


class AbstractUploader(ABC):
    """将文件上传，先指定用的软件路径和上传的位置"""
    def __init__(self, app, server_path):
        self.server_path = server_path
        self.app = app
        self.filenames = []

    def import_config(self, filepaths, item_name):
        self.filepaths = filepaths
        self.item_name = item_name
        self.item_upload_path = self.server_path + '/' + self.item_name

    @abstractmethod
    def uploading(self, filepath, filename):
        """上传"""
        raise NotImplementedError

    @abstractmethod
    def get_uploaded_files_link(self):
        """获取文件的下载链接"""
        raise NotImplementedError

    def run(self):
        """调用以上命令，串联工作流程"""
        if isinstance(self.filepaths, str):
            self.filepaths = [self.filepaths]

        for filepath in self.filepaths:
            filename = os.path.basename(filepath)
            self.filenames.append(filename)
            self.uploading(filepath)
            print(f"{self.item_name} new file {filename} have upload to server")


class MinioUploader(AbstractUploader):
    """上传到 minio"""
    def __init__(self, app, server_path, minio_server_path):
        super().__init__(app, server_path)
        self.minio_server_path = minio_server_path

    def uploading(self, filepath):
        # 每个路径，一个文件夹
        subprocess.run([self.app, 'mb', "--ignore-existing", self.item_upload_path])
        subprocess.run([self.app, 'cp', filepath, self.item_upload_path])
        print("Uploaded file:", filepath)

    def get_uploaded_files_link(self):
        server_path = self.server_path.split("/")[1] + '/' + self.item_name
        string = self.minio_server_path
        if self.minio_server_path.endswith("/"):
            string = self.minio_server_path[:-1]
        uploaded_files_link = [f"http://{string}/{server_path}/{file}" for file in self.filenames]
        self.filenames = []   # 否则，前个软件下载的链接，会到后面的里
        return uploaded_files_link

    def delete(self, section_name, filename):
        filepath = f"{self.server_path}/{section_name}/{filename}"
        subprocess.run([self.app, 'rm', filepath])
