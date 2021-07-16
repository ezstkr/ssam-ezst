from django.urls import path
from . import views

app_name = 'lecture'

urlpatterns = [
    # path('list/<int:pk_course>/', views.LectureList.as_view()), # Course Detail 로 대체
    path('create/', views.LectureCreate.as_view()),
    path('<int:pk>/', views.LectureDetail.as_view()),
    path('<int:pk>/update/', views.LectureUpdate.as_view()),
    path('<int:pk>/delete/<int:pk_course>', views.delete_lecture),
]