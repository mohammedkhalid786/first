from django.shortcuts import render

# Create your views here.

from django.views import *


def jampandu(request):
    return HttpResponse('hi jampandu how are you')