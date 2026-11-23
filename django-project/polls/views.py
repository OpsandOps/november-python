# from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from polls.models import Question, Choice
from django.shortcuts import render, get_object_or_404, redirect
# from django.template import loader
from .forms import QuestionForm, ChoiceForm, ChoiceFormSet

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

def create_question(request):
    #1. check for the form http method and
    #  create an instance of the form with the request body
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        #2. check if the form is valid
        # create an instance of the question from the form inputs
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect(
                'polls:details',
                question_id=question.id
            )
    else:
        #3. if not valid, return an instance of the form object using the form.html
        form = QuestionForm()
    return render(request, 'polls/question_form.html', {'form': form})

def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #1. check form method
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('polls:details', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
        formset = ChoiceFormSet(instance=question)
    return render(request, 'polls/question_form.html', {
        'form': form,
        'formset': formset,
        'question': question
    })

def add_choice_to_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        choiceform = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('polls:details', question_id=question.id)
    else:
        form = ChoiceForm(initial={'question':question})
    return render(request, 'polls/question_form.html', {'form': choiceform, 'question': question})




