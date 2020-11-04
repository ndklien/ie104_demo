from django import forms
from .models import Question

class PushQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', )
