from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Article, ArticleSection

from django.views import generic

class ArticleView(generic.DetailView):
    model = Article
    template_name = "sh_app/article2.html"



def galazar404(request, exception):
    return render(request, 'sh_app/galazar404.html', status=404)



def article_page(request, article_id):

    print("article_id = "+str(article_id))

    content = """
    <p> Rzaba okumkawa </p>
    <p> Szukasz artykułu z id = {}
    <p style="color:green;"> Zalogowany użytkownik {} </p>
    """

    user_name = "NOT LOGGED IN"
    if request.user.is_authenticated:
        user_name = request.user.username

    context = {"content1": content.format(article_id, user_name),
                "title1": "rzaba"}

    return render(request , "sh_app/article_generic1.html", context)

