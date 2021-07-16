from django.urls import path
from . import views

urlpatterns = [
    path('update_course/<int:pk>/', views.CourseUpdate.as_view()),
    path('delete_course/<int:pk>/', views.delete_course),
    path('create_course/', views.CourseCreate.as_view()),
    path('', views.CourseList.as_view()),
    path('<int:pk>/', views.CourseDetail.as_view()),
]