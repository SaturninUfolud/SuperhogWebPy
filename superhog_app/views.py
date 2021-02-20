from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from django.template import loader



def index(request):
    return render(request, "sh_app/index.html")

def superhog_main(request):
    return render(request, "sh_app/superhog.html")