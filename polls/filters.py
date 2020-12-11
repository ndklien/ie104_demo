import django_filters

from .models import Question, Choice

class QuestionFilter(django_filters.FilterSet):

    class Meta:
        model = Question
        fields = [
            'question_text'
        ]