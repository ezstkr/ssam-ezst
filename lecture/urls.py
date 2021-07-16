from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('list/<int:pk_course>/', views.lecture_list),
    path('<int:pk_lecture>/', views.lecture_detail),
    path('create/', views.LectureCreate.as_view()),
#     path('update/', views.), # 개발 대기 중

    path('', views.lecture_list),
    path('list/', views.lecture_list),
]

# path('<int:pk_course>/', views.LectureList.as_view(), name='list'),