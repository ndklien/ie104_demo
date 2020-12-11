from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers

from .forms import PushQuestionForm, QuestionForm
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.db.models import Q

from .filters import QuestionFilter

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
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        HttpResponse('Error.')
    selected_choice.votes += 1
    selected_choice.save()
    return render(request, 'polls/base_results.html', {'question': question})
    
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

class Search_results(generic.ListView):
    model = Question
    template_name = 'polls/base_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Question.objects.filter(
            Q(question_text__icontains=query)
        )

def postQuestion(request):
    if request.is_ajax and request.METHOD == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid:
            instance = form.save()

            ser_instance = serializers.serialize('json', [instance, ])
            data_context = {
                "instance": ser_instance
            }
            return JsonResponse(data_context, status=200)
        else:
            data_context = {
                "error": form.errors
            }
            return JsonResponse(data_context, status=400)
    else: return JsonResponse({"error": ""}, status=400)

def recommendQuestion(request):
    quest = Question.objects.all()

    questF = QuestionFilter(request.GET, queryset=quest)
    # arr = []
    # count = 0
    # for quest in questF.qs:
    #     if count < 3:
    #         arr.append(quest)
    #         count += 1
    #     else:
    #         break

    context = {
        'questionList': questF, 
    }
    return render(request, 'polls/base_recommend.html', context)




