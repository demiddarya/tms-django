from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, Http404

from .models import Question, Choice


# Create your views here.


def index(request: HttpRequest):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    try:
        question = get_object_or_404(Question, id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    choice_id = int(request.POST['choice_id'])
    selected_choice = question.choices.get(id=choice_id)
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('polls:detail', question.id)
