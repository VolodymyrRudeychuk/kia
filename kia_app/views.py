from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import (
    Front,
    Category,
    Media,
    # Message,
)

from django.contrib.auth import logout
from models import Statistic


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

from .forms import TokenForm, MessageForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# @login_required
@csrf_exempt
def home(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TokenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.login_user(request)
            Statistic.objects.create(token=form.token)
            return HttpResponseRedirect('/catalog/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TokenForm()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        message_form = MessageForm(request.POST)
        # check whether it's valid:
        if message_form.is_valid():
            message_form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        message_form = MessageForm()


    return render(request, 'home.html', {
        'front': Front.objects.first(),
        'message_form':  message_form,
        'token_form': form,
    })


def catalog(request):
    category_id = int(request.GET.get('category', 3))
    language = int(request.GET.get('language', 1))
    category = Category.objects.get(id=category_id)
    media = Media.objects.filter(category=category, category__language=language)
    video_categories = Category.objects.filter(type=1, language=language)
    audio_categories = Category.objects.filter(type=2, language=language)

    return render(request, 'catalog.html', {
        'current_language': language,
        'current_category': category,
        'audio_categories': audio_categories,
        'video_categories': video_categories,
        'media': media})



# @csrf_exempt
# def send_email(request):
#     print request.POST
#     form = MessageForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse('Good boy!')
#     else:
#         return HttpResponseBadRequest('Bad boy!')