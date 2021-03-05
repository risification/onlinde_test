from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', poll_page, name='poll'),
    path('questions/<int:id_poll>/', question_page, name='question'),
    path('choices_answer/<int:id_question>/', choice_answer_page, name='choice_answer')
]
