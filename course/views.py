from django.shortcuts import render, redirect
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
            form.instance.author = current_user
            response = super(CourseCreate, self).form_valid(form)

            return response

        else:
            return redirect('/course/')


class CourseDetail(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data()

        return context


class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'content', 'head_image', 'file_upload']

    template_name = 'blog/course_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdate, self).get_context_data()

        return context
