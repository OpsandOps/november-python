from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date-published")

    def __str__(self):
        """a string repr for the object"""
        return f"""\n
                [QUESTION]:  {self.question_text} 
                """

    # =======================================
    def check_question(self):
        question_list = []
        if self.question_text.startswith("What is"):
            question_list.append(self.question_text)
            for i in enumerate(question_list):
                print(i)
        else:
            return None

    # =========================================
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=50)

    def __str__(self):
        return str(self.votes)


    @property
    def add_votes(self):
        return self.votes + 10


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __repr__(self):
    #     return self.name