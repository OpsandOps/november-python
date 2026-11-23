from django.urls import path
from polls import views 

app_name = "polls"

urlpatterns = [
    # polls/
    # path('index/', views.index, name='index'),
    # path('json/', views.jsonView, name='json'),
      # ex: /polls/
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="details"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("data/", views.data, name="data"),
    path("forms/", views.create_question, name='question_form'),
    path("<int:question_id>/edit/", views.edit_question, name='edit_question'),
]



