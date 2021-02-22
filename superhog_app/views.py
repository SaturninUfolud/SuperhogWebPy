from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views import generic


import os

from .models import Article, ArticleSection
from .forms import UploadFileForm


UPLOAD_FILES_DIRECTORY = "/superhog_app/static/sh_app/upload"



class ArticleView(generic.DetailView):
    model = Article
    template_name = "sh_app/article2.html"



def galazar404(request, exception):
    return render(request, 'sh_app/galazar404.html', status=404)

def upload_file(request):

    if request.user.is_authenticated:

        user_name = request.user.user_name

        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():



                return HttpResponseRedirect('/index')
            else:
                form = UploadFileForm()

        return render(request, 'upload.html',
        {'user': request.user.user_name,
        'form': form})

    else:

        logs = [
            "Żaden użytkownik nie jest zalogowany.",
            "Proszę się zalogować na <a href = \"/admin\"> stronie administracyjnej </a>",
        ]


        return render(request, "error_page.html",
        {
            "logs":logs,
            "title":"Prosię się zalogować",
        })


def article_page_test(request, article_id):

    print("article_id = "+str(article_id))

    content = """
    <p> Rzaba okumkawa </p>
    <p> Szukasz artykułu z id = {}
    <p style="color:green;"> Zalogowany użytkownik {} </p>
    <p> {} </p>
    """

    user_name = "NOT LOGGED IN"
    if request.user.is_authenticated:
        user_name = request.user.username

    context = {"content1": content.format(article_id, user_name,"czesio.png"),
                "title1": "rzaba"}

    #f = open("rzaba.txt", "a")
    #f.write("Now the file has more content!")
    #f.close()


    return render(request , "sh_app/article_generic1.html", context)

