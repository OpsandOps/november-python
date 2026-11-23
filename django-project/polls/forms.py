from django import forms
from django.forms import inlineformset_factory
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["pub_date", "question_text"]

        labels = {
            'question_text': 'Enter your question here',
            'pub_date': 'Publication date'
        }
        help_texts = {
            'question_text': 'Maximum of 255 chars',
            'pub_date': 'select when this question is published'
        }
        error_messages = {
            'question_text': {
                'required': 'Please enter a question',
                'max_length': 'Question is too large/long'
            }
        }
        widgets = {
            'question_text': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': 'type your question here...',
                'class': 'form-control',
            }),
            'pub_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            })
        }

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'votes']
        widgets = {
            'choice_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your choice text here'
            }),
            'votes': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder':'vote here',
                'min': 0,
            }),
        }

# Inline formset for handling multiple choices with a question
ChoiceFormSet = inlineformset_factory(
    Question, 
    Choice, 
    form=ChoiceForm,
    extra=2,
    can_delete=True
)
