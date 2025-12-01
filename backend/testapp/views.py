from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    t = render_to_string('testapp/main.html')
    return HttpResponse(t)

def quiz(request, quiz_id):
    if quiz_id == 1:
        t = render_to_string('testapp/quiz.html')
        return HttpResponse(t)
    else:
        raise Http404()

def rating(request):
    t = render_to_string('testapp/rating.html')
    return HttpResponse(t)

def page_not_found(reques, exception):
    return HttpResponseNotFound("<h1>Страница не найдена!</h1>")