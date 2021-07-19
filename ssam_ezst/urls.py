from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from course import views

urlpatterns = [
    path('course/', include('course.urls')),
    path('lecture/', include('lecture.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.CourseList.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = '이지쌤 관리자 페이지'