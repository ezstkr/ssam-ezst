from django.db import models
from django.contrib.auth.models import User
from lecture.models import Lecture


class Course(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='course/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    lectures = models.ManyToManyField(Lecture, blank=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.creator}'

    def get_absolute_url(self):
        return f'/course/{self.pk}/'


