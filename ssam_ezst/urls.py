from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('course/', include('course.urls')),
    path('admin/', admin.site.urls),
]
