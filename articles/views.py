from django.shortcuts import render
from .models import Article, Comment


def articles_list(request):
    a_list = Article.objects.all().order_by('-id')

    return render(request, 'home.html', {"article_list": a_list})


def single_article(request, art_id):
    comments = Comment.objects.filter(article__id=art_id)
    article = Article.objects.get(pk=art_id)

    return render(request, 'comments.html', {"comments_list": comments, 'article': article})
