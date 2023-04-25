from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, Http404
from .models import Article

# Create your views here.


def index(request: HttpRequest):
    articles = Article.objects.all
    context = {'articles_list': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id: int):
    try:
        article = get_object_or_404(Article, id=article_id)
    except Article.DoesNotExist:
        raise Http404('Question does not exist')
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def like(request, article_id: int):
    assert request.method == 'POST'
    article_id = request.POST['article_id']
    article = get_object_or_404(Article, id=article_id)
    article.like_count += 1
    article.save()
    return redirect('articles:detail', article.id)
