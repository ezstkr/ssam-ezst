from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseList.as_view()),
]