from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def polls(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# Create your views here.
