from django import forms
from .models import Question

class PushQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', )

class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

        class Meta:
            model = Question
            fields = ("__all__")
