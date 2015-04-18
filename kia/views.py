from django.shortcuts import render
from .models import (
    Front,
    # Message,
)
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm


# class MessageForm(ModelForm):
#     class Meta:
#         model = Message


def home(request):
    context = {
        'front': Front.objects.first(),
    }
    template = 'home.html'
    return render(request, template, context)


# @csrf_exempt
# def send_email(request):
#     print request.POST
#     form = MessageForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse('Good boy!')
#     else:
#         return HttpResponseBadRequest('Bad boy!')