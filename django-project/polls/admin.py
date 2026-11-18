from django.contrib import admin
from unfold.admin import ModelAdmin
from polls.models import Question, Choice
from django import forms

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("PUBLICATION NAME", {
            "classes": ["collapse"],
            "fields": ["pub_date"]

        }),
        ("QUESTION", {
            "classes": ["collapse"],
            "fields": ["question_text"]

        })
    ]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "CHOICE", {
                "classes": ["collapse"],
                "fields": ["question", "votes", "choice_text"]
            }
        ),
    ]

# class ChoiceForm(forms.ModelForm):
#     class Meta:
#         model = Choice
#         exclude = ["question"]

# class ChoiceAdmin(admin.ModelAdmin):
#     exclude = ["question"]
#     form = ChoiceForm

# admin.site.register(Choice, ChoiceAdmin)



