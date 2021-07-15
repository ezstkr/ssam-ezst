from django.db import models
from django.contrib.auth.models import User


class Lecture(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    head_image = models.ImageField(upload_to='lecture/images/%Y/%m/%d/', blank=True)

    content = models.TextField()
    slide = models.TextField()

    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.creator}'

    def get_url(self):
        return f'/lecture/{self.pk}/'



