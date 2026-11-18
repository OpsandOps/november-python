from polls.models import Question, Choice, Author
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

def run():
    # ===============Creating Records (without the model manager)=====
    # record21 = Question(
    #     question_text="what is composition in python",
    #     pub_date=timezone.now()
    # )
    # record21.save()

    # # accessing a record created in the database
    # print(f"[RECORD ONE]: {record1}")
    # print(f"{record1.question_text}")
    # print(f"{record1.pub_date}")

    # =============creating a record using the model manager=========
    # objects - ModelManager - interfaces exposes functions to perform specific operations
    # create
    # date = timezone.now()
    # record = Question.objects.create(
    #     question_text="what is a model manager in python",
    #     pub_date=date
    # )
    # print(f"[NEW RECORD ]: {record}")

    # ================records for choice using model manager ==========
    # question1 = Question.objects.get(pk=1)
    # choice = Choice.objects.get(pk=6)
    # print(choice.add_votes)
    # ==================================get/get-or-create====================
    # record20 = Question.objects.get(pk=25)
    # print(record20)
    # ===============================filter=======================
    # all_questions = Question.objects.filter(question_text__startswith="What is")
    # print(all_questions)
    # ===========================
    # record20 = Question.objects.get(id=19)
    # print(type(record20.pub_date))
    # record20.pub_date > datetime.datetime.now()
    
    # ====================================
    # using a helper function to check a record
    # =========================================
    # records = Question.objects.get(pk=11)
    # print(records.check_question())

    # wa_published_recently
    # question = Question.objects.get(pk=5)
    # print(question.was_published_recently())

    # ===create an author
    user = User.objects.first()
    print(user)
    author = Author.objects.create(
        name=user
    )
    print(author)

    

   

