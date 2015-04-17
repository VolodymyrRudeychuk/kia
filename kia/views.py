from django.shortcuts import render
from .models import (
    Front,
)


def home(request):
    context = {
        'front': Front.objects.first(),
    }
    template = 'home.html'
    return render(request, template, context)