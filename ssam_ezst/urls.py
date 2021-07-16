from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('course/', include('course.urls')),
    path('lecture/', include('lecture.urls')),
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
]

# _media 폴더 경로 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)