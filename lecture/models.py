from django.db import models
from django.contrib.auth.models import User
import os


class Lecture(models.Model):
    title = models.CharField(max_length=30)
    head_image = models.ImageField(upload_to='lecture/images/%Y/%m/%d/', blank=True)

    content = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/lecture/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    class Meta:
        ordering = ['title']


class Slide(models.Model):
    image = models.ImageField(upload_to='slide/images/%Y/%m/%d/', blank=True)
    content = models.TextField(blank=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'[{self.pk}] {self.image.name}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

