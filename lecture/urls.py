from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('<int:pk_course>/', views.lecture_list),
    path('create/', views.LectureCreate.as_view()),
#     path('update/', views.), # 개발 대기 중
#     path('<int:pk>/', views.),
]

# path('<int:pk_course>/', views.LectureList.as_view(), name='list'),