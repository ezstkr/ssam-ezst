from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Course
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify


class CourseList(ListView):
    model = Course
    ordering = '-pk'
    
    def get_context_data(self, **kwargs):
        context = super(CourseList, self).get_context_data()

        return context


class CourseCreate(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Course
    fields = ['title', 'content', 'head_image']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.creator = current_user
            response = super(CourseCreate, self).form_valid(form)

            return response

        else:
            return redirect('/course/')


class CourseDetail(DetailView):
    model = Course
    # fields = ['lectures']

    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data()
        return context


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title','creator', 'lectures', 'content', 'head_image']

    template_name = 'course/course_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdate, self).get_context_data()
        return context


def delete_course(request, pk):
    course = Course.objects.get(pk=pk)

    if request.user.is_authenticated and (request.user == course.creator or request.user.is_superuser):
        course.delete()
        return redirect('/course/')
    else:
        raise PermissionDenied


def remove_lecture_from_course(request, pk_course, pk_lecture):
    course = Course.objects.get(pk=pk_course)

    if request.user.is_authenticated and (request.user == course.creator or request.user.is_superuser):
            lecture = course.lectures.get(pk=pk_lecture)
            course.lectures.remove(lecture)
            return redirect(f'/course/{pk_course}')
    else:
        raise PermissionDenied
