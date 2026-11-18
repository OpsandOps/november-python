# from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404
# from django.template import loader


def index(request):
    question = Question.objects.order_by("-pub_date")
    return render(request, "polls/index.html", {"question": question})

# def _getInfo(**args):
#     username = input("Enter your name: ")
#     firstname = input("Enter firstname: ")
#     return(f"""
#     [USERNAME]: {username}
#     [FIRSTNAME]: {firstname}
#     """)

# def jsonView(request):
#     result = _getInfo()
#     return JsonResponse(
#         result, safe=False
#     )def index

def detail(request, question_id):
    question = get_object_or_404(
        Question, 
        pk=question_id, 
    )
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"The question with id {question_id} does not exist")
    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/voteform.html', {'question': question})

def data(request):
    myBio = {
        "name": "Prospa",
        "class": "Django"
    }
    mylist = ["daniel", "shedrack", "praise", "perculiar"]
    return render(request, "polls/data.html", {"data": mylist})