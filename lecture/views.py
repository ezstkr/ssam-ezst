from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionDenied
from course.models import Course
from lecture.models import Lecture, Slide


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

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data()
        context['create'] = True

        return context


class LectureDetail(DetailView):
    model = Lecture
    template_name = 'lecture/detail.html'

    def get_context_data(self, **kwargs):
        context = super(LectureDetail, self).get_context_data()

        lecture = Lecture.objects.get(pk=self.kwargs['pk'])
        context['lecture'] = lecture
        context['slides'] = lecture.slide_set.all()

        return context


class LectureUpdate(LoginRequiredMixin, UpdateView):
    model = Lecture
    fields = ['title', 'content', 'head_image']

    template_name = 'lecture/create.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(LectureUpdate, self).form_valid(form)

            return response

        else:
            return redirect('/course/')


def delete_lecture(request, pk, pk_course):
    lecture = Lecture.objects.get(pk=pk)
    course = Course.objects.get(pk=pk_course)

    if request.user.is_authenticated and request.user == course.creator:
        lecture.delete()
        return redirect(f'/course/{pk_course}')
    else:
        raise PermissionDenied