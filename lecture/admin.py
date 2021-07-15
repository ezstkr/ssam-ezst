from django.contrib import admin
from .models import Lecture, Slide


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 5


class LectureAdmin(admin.ModelAdmin):
    inlines = [SlideInline]


admin.site.register(Lecture, LectureAdmin)
