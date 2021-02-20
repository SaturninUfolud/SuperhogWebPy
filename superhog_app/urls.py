from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from . import views

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect(reverse('sh_app:index'))),

    path('index', views.index, name='index'),
    path('superhog', views.superhog_main, name="superhog"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('sh_app/favicon.ico')))
]

app_name = 'sh_app'