from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Question

@login_required
def polls(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})

@login_required
def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

@login_required
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

@login_required
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
