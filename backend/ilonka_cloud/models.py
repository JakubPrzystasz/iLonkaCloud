from django.db import models
from django.contrib.auth.models import User


# def paper_directory_path(instance, filename):
#     _filename = filename.split('.')
#     filename = re.sub(r'\W+', '', _filename[0])
#     filename = filename.replace(' ','_')
#     filename = textwrap.shorten(filename,width=100,placeholder='')
#     filename += f'.{_filename[-1]}'
#     return f'paper_files/paperNo.{instance.paper.pk}/{filename}'


# Create your models here.
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(blank=True, max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
