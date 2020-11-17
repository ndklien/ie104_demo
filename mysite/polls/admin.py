from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin:
    fieldset = [
        (None, {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')



admin.site.register(Question)
admin.site.register(Choice)
