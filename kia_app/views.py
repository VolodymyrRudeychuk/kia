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


@csrf_exempt
def home(request):
    if request.method == 'POST' and request.POST.get('token') is not None:
        # create a form instance and populate it with data from the request:
        print request.POST
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
        'grades': Category.GRADES
    })


@login_required
@csrf_exempt
def catalog(request):
    language = int(request.GET.get('language', 1))
    category_id = request.GET.get('category', None)
    grade = request.GET.get('grade', 0)

    if category_id is None:
        category = Category.objects.filter(language=language, grade=grade).first()
    else:
        category = Category.objects.get(id=int(category_id), grade=grade)

    media = Media.objects.filter(category=category, category__language=language, category__grade=grade)
    video_categories = Category.objects.filter(type=1, language=language, grade=grade)
    audio_categories = Category.objects.filter(type=2, language=language, grade=grade)

    return render(request, 'catalog.html', {
        'current_language': language,
        'current_category': category,
        'audio_categories': audio_categories,
        'video_categories': video_categories,
        'media': media,
        'grade': grade})



# @csrf_exempt
# def send_email(request):
#     print request.POST
#     form = MessageForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse('Good boy!')
#     else:
#         return HttpResponseBadRequest('Bad boy!')