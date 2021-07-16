from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from course.models import Course


def lecture_list(request, pk_course):
    courses = Course.objects.all()
    course = Course.objects.get(pk=pk_course)

    return render(
        request,
        'lecture/list.html',
        {
            'courses': courses,
            'course': course,
            'lectures': course.lectures,
            'side_widgets': True,
        },
    )


# class LectureList(ListView):
#     model = Course
#
#     template_name = 'lecture/list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ListView, self).get_context_data()
#         context['courses'] = Course.objects.all()
#         context['course'] = Course.objects.get(pk=pk_course)
#         context['lectures'] = context['course'].lectures
#
#         return context


class LectureCreate(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Course
    fields = ['title', 'content', 'head_image']

    template_name = 'lecture/create.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(LectureCreate, self).form_valid(form)

            return response
        else:
            return redirect('/lecture/')

    def get_context_data(self, **kwargs):
        context = super(LectureDetail, self).get_context_data()

        return context


class LectureDetail(DetailView):
    model = Course

    template_name = 'lecture/detail.html'

    def get_context_data(self, **kwargs):
        context = super(LectureDetail, self).get_context_data()

        return context


class LectureUpdate(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'content', 'head_image', 'file_upload']

    template_name = 'lecture/update.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(LectureCreate, self).form_valid(form)

            return response

        else:
            return redirect('/course/')

    def get_context_data(self, **kwargs):
        context = super(LectureUpdate, self).get_context_data()

        return context

