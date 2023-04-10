from django.shortcuts import render
from django.http import HttpRequest, Http404

from .models import Question
# Create your views here.


def index(request: HttpRequest):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def detail(request, question_id: int):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
