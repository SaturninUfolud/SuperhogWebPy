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
    
    path('creatures', views.CreaturesListView.as_view(), name ="creatures"),
    path('gallery', views.GalleryView.as_view(), name = "gallery"),
    path('content_list', views.ContentListView.as_view(), name = "content_list"),

    path('article<int:pk>', views.ArticleView.as_view(), name = "article"),
    
    path('test_galazar404', lambda request: render(request, "sh_app/galazar404.html"), name="test_galazar404"),
    path('test_article<int:article_id>', views.article_page_test, name = "article_test"),
]

app_name = 'sh_app'
