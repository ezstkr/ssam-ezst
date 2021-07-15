from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from course.models import Course


def lecture_list(request, pk_course):
    courses = Course.objects.all()
    course = Course.objects.get(pk=pk_course)

    return render(
        request,
        'lecture/lecture_list.html',
        {
            'courses': courses,
            'course': course,
            'lectures': course.lectures,
        },
    )