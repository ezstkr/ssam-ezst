from django.urls import path
from . import views

urlpatterns = [
    path('update_course/<int:pk>/', views.CourseUpdate.as_view()),
    path('create_course/', views.CourseCreate.as_view()),
    path('', views.CourseList.as_view()),
    path('<int:pk>/', views.CourseDetail.as_view()),
]