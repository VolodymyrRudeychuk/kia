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

from .forms import LoginOrRequest
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    if request.method == 'POST' and request.POST.get('password') is not None:
        # create a form instance and populate it with data from the request:
        form = LoginOrRequest(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if form.cleaned_data['password']:
                form.login_user(request)
                Statistic.objects.create(user=form.school)
                return HttpResponseRedirect('/')
            elif form.cleaned_data['email']:
                form.send_message()
                return HttpResponseRedirect('/?success=1')
            else:
                form.login_user(request)
                Statistic.objects.create(user=form.school)
                return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginOrRequest()

    return render(request, 'home.html', {
        'front': Front.objects.first(),
        'login_form': form,
        'grades': Category.GRADES,
        'success': request.GET.get('success')
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