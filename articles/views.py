from django.shortcuts import render
from django.http import HttpRequest
from .models import Article

# Create your views here.


def index(request: HttpRequest):
    articles = Article.objects
    context = {'article_list': }
    return
