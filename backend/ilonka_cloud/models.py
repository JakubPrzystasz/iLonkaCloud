from django.db import models
from django.contrib.auth.models import User
import re
import textwrap

from django.db.models.signals import pre_delete


def file_directory_path(instance, filename):
    _filename = filename.split('.')
    filename = re.sub(r'\W+', '', _filename[0])
    filename = filename.replace(' ', '_')
    filename = textwrap.shorten(filename, width=100, placeholder='')
    filename += f'.{_filename[-1]}'
    return f'users_file/userId.{instance.user.pk}/{filename}'


# Create your models here.
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_directory_path, blank=True, max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def delete_file_with_object(instance, **kwargs):
    """
    Deletes files from system when UploadedFile object is deleted from database
    :param instance: UploadedFile object (file that is being deleted)
    :param kwargs:
    :return:
    """
    instance.file.delete()


pre_delete.connect(delete_file_with_object, sender=UploadedFile)
