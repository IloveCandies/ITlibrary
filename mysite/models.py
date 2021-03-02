from django.db import models

class UploadFileModel(models.Model):
    description = models.CharField(max_length=150)
    file = models.FileField(upload_to='media/documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)