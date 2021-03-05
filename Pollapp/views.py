from django.shortcuts import render
from .models import Poll, Question
from .forms import AnswerForm
from django.http import HttpResponse

# Create your views here.

def poll_page(request):
    poll = Poll.objects.all()
    return render(request, 'Poll/poll.html', {'poll': poll})


def question_page(request, id_poll):
    poll = Poll.objects.get(id=id_poll)
    question = poll.question_set.all()
    return render(request, 'Poll/question.html', {'questions': question})


def choice_answer_page(request, id_question):
    total = 0
    question = Question.objects.get(id=id_question)
    choice = question.choiceansw_set.all()
    form = AnswerForm(initial={'question': question})
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            if question.true_answer == form.cleaned_data['answer']:
                question.poll.points+= 5
                question.poll.save()
                return  HttpResponse('правильный ответ ')
    return render(request, 'Poll/choice_answer.html',
                  {'choices': choice, 'questions': question, 'form': form, 'total': total})
