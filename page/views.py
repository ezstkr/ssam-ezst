from django.shortcuts import render
from course.models import Course


def landing(request):
    recent_courses = Course.objects.order_by('-pk')[:3]
    return render(
        request,
        'page/landing.html',
        {
            'recent_courses': recent_courses,
        }
    )
