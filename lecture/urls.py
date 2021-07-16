from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('list/<int:pk_course>/', views.LectureList.as_view()),
    path('<int:pk>/', views.LectureDetail.as_view()),
    path('create/', views.LectureCreate.as_view()),
    path('<int:pk>/update/', views.LectureUpdate.as_view()),
#     path('delete/', views.), # 개발 대기 중

    path('', views.LectureList.as_view()),
    path('list/', views.LectureList.as_view()),
]

# path('<int:pk_course>/', views.LectureList.as_view(), name='list'),