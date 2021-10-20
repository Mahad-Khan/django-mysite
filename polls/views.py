from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question
from django.shortcuts import render, get_object_or_404

# def index(request):
#     latest_question_list = Question.objects.all()
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     print(context)
#     return HttpResponse(template.render(context, request))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# # detail(request=<HttpRequest object>, question_id=34)
# def detail(request, question_id):
#     try:
#         print(Question.objects.get(pk=2))
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


# The get_object_or_404() function takes a Django model as its first argument and an\
# arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager.\
#  It raises Http404 if the object doesn’t exis
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# returning an HttpResponse object containing the content for the requested page, 
# or raising an exception such as Http404. The rest is up to you.
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)