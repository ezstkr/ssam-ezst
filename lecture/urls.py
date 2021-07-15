from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    path('<int:pk_course>/', views.lecture_list, name='lecture_list'),
#     path('create/', views.), # 개발 대기 중
#     path('update/', views.),
#     path('<int:pk>/', views.),
]
