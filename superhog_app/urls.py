from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from django.shortcuts import render


from . import views

from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect(reverse('sh_app:index'))),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('sh_app/favicon.ico'))),

    path('index', lambda request: render(request,"sh_app/index.html"), name='index'),
    path('superhog', lambda request: render(request,"sh_app/superhog.html"), name="superhog"),

    path('contact_me', lambda request: render(request,"sh_app/contact_me.html"), name="contact_me"),
    path('ropucha', lambda request: render(request,"sh_app/ropucha.html"), name="ropucha"),
    path('elephant', lambda request: render(request,"sh_app/elephant.html"), name="elephant"),
    path('levels_editor', lambda request: render(request,"sh_app/levels_editor.html"), name="levels_editor"),
    path('test', lambda request: render(request, "sh_app/test1.html"), name="test"),

    path('article<int:pk>', views.ArticleView.as_view(), name = "article"),
    path('article_test<int:article_id>', views.article_page_test, name = "article_test"),
]

app_name = 'sh_app'
