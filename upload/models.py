from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Upload(models.Model):
    path = models.CharField(max_length=20)  # Random string for the path
    file_name = models.CharField(max_length=255)  # Original filename
    suffix_name = models.CharField(max_length=10, blank=True)  # File extension
    link = models.URLField()  # Download link from MinIO
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of upload

    def is_expired(self):
        return datetime.now() >= self.uploaded_at + timedelta(days=3)
    
    def is_photo(self):
        if self.suffix_name in {".png", ".jpg", ".jpeg", ".webp", '.gif', '.avif', '.svg'}:
            return True
        else:
            return False

