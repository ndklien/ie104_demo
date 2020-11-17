from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PushQuestionForm
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

question_list = Question.objects.all()

#print out all questions:

def home(request):
    return render(request, 'polls/base_home.html')

def owner(request):
    return HttpResponse("This is my first Django project")

"""def index(request):
    context = {'question_list': question_list}
    return render(request, 'polls/base_index.html', context)"""

class IndexView(generic.ListView):
    template_name = 'polls/base_index.html'
    context_object_name = 'question_list'
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/base_detail.html'

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/base_detail.html', {'question': question, })

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/base_results.html'

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = { 
        'question': question,
        'error_message': "You didn't select a choice.",
    }
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', context)
    selected_choice.votes += 1
    selected_choice.save()
    return render(request, 'polls/base_results.html', context)
    
def addNewQuestion(request):
    question = PushQuestionForm()    
    return render(request, 'polls/base_addQuestion.html', {'question': question })

def saveNewQuestion(request):
    if request.method == 'POST':
        g = PushQuestionForm(request.POST)
        if g.is_valid():
            notiupload = 'Upload succeed.'
            g.save()
        else:
            notiupload = 'Upload failed.'
    else:
        return HttpResponse('Not POST request.')
    return render(request, 'polls/base_NotiUpload.html', {'notiupload': notiupload})

def chooseQuestion(request):
    pass