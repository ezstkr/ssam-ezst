from django.shortcuts import render
from lecture.models import Lecture, Slide


def landing(request):
    slides = Slide.objects.all()[:5]
    return render(
        request,
        'page/landing.html',
        {
            'slides': slides
        }
    )
