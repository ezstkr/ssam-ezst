from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from course.models import Course
from lecture.models import Lecture


class LectureList(ListView):
    model = Course
    template_name = 'lecture/list.html'

    def get_context_data(self, **kwargs):
        context = super(LectureList, self).get_context_data()
        context['courses'] = Course.objects.all()
        context['course'] = Course.objects.get(pk=self.kwargs['pk_course'])
        context['lectures'] = context['course'].lectures
        context['side_widgets'] = True

        return context


class LectureCreate(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Lecture
    fields = ['title', 'content', 'head_image']

    template_name = 'lecture/create.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(LectureCreate, self).form_valid(form)

            return response
        else:
            return redirect('/course/')


class LectureDetail(DetailView):
    model = Lecture
    template_name = 'lecture/detail.html'

    def get_context_data(self, **kwargs):
        context = super(LectureDetail, self).get_context_data()
        context['lecture'] = Lecture.objects.get(pk=self.kwargs['pk'])
        context['side_widgets'] = False

        return context


class LectureUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'content', 'head_image']

    template_name = 'lecture/update.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(LectureUpdate, self).form_valid(form)

            return response

        else:
            return redirect('/course/')

