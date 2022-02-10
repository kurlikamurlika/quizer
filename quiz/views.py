from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Quiz, Question, Answer, Play
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random
# Create your views here.

def index(request):
    quiz_list_time = Quiz.objects.order_by('-pub_date')

    quiz_dict = []
    play_list = Play.objects.all()
    question_list = Question.objects.all()

    for quiz in quiz_list_time:
        quiz_dict.append([quiz, quiz.pub_date.strftime('%d.%m.%y'), 0, 0])
    for j in range(len(quiz_list_time)):
        for play in play_list:
            if play.quiz_id == quiz_list_time[j].id:
                quiz_dict[j][2] += 1

    for j in range(len(quiz_list_time)):
        for question in question_list:
            if question.quiz_id == quiz_list_time[j].id:
                quiz_dict[j][3] += 1

    sorted_quiz_plays = sorted(quiz_dict, key=lambda x: x[2], reverse=True)
    quiz_plays = sorted_quiz_plays[::-1]
    sorted_quiz_length = sorted(quiz_dict, key=lambda x: x[3], reverse=True)
    quiz_length = sorted_quiz_length[::-1]
    quiz_time = quiz_dict[::-1]
    return render(request, 'quiz/index.html', context={'quiz_plays_descending': sorted_quiz_plays, 'quiz_length_descending': sorted_quiz_length, 'quiz_time_descending': quiz_dict, 'quiz_plays_ascending': quiz_plays, 'quiz_length_ascending': quiz_length, 'quiz_time_ascending': quiz_time})

def profile(request, user_id):
    user_profile = User.objects.get(pk=user_id)
    quiz_list = Quiz.objects.filter(user_id=user_id)
    play_list = Play.objects.filter(user_id=user_id)
    return render(request, 'quiz/profile.html', context={'quiz_list': quiz_list, 'play_list': play_list, 'user_profile': user_profile})

def about(request):
    return render(request, 'quiz/about_us.html', context={})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('quiz:index')
    else:
        form = SignUpForm()
    return render(request, 'quiz/register.html', {'form': form})



def play(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    question_list = quiz.question_set.all()
    return render(request, 'quiz/play.html', context={"quiz": quiz, "question_list": question_list})

def result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    points = 0
    question_list = quiz.question_set.all()

    for question in question_list:
        selected_answer = question.answer_set.get(pk=request.POST[f'answer{question.id}'])
        points += selected_answer.points

    play = Play(quiz_id=quiz.id, points=points, user_id=request.user.id)
    play.save()
    play_list = Play.objects.filter(quiz_id=quiz_id).order_by("-points")
    play_list = list(play_list)
    for i in play_list:
        for j in play_list:
            if j.user.username == i.user.username:
                if j.points > i.points:
                    pass


    return render(request, 'quiz/result.html', context={'points': points, 'play_list': play_list})

def create(request):
    return render(request, 'quiz/create_test.html', context={})

def edit(request):
    quiz_name = request.POST['quiz_name']
    quiz = Quiz(user_id=request.user.id, quiz_name=quiz_name, pub_date=timezone.now())
    quiz.save()
    question_number = abs(int(request.POST['question_number']))
    answer_number = abs(int(request.POST['answer_number']))
    return render(request, 'quiz/edit.html', {'quiz_name': quiz_name, 'question_number': question_number, 'answer_number': answer_number, 'range_question': range(question_number), 'range_answer': range(answer_number)})

def upload_test(request, question_number, answer_number):
    for i in Quiz.objects.all():
        quiz = i
    quiz_id = quiz.id
    for i in range(question_number):
        question_text = request.POST[f'question_text{i}']
        question = Question(quiz_id=quiz_id, question_text= question_text)
        question.save()
        for j in range(answer_number):
            answer_text = request.POST[f'answer_text_{i}_{j}']
            points = request.POST[f'answer_points_{i}_{j}']
            answer = Answer(question_id=question.id, answer_text=answer_text, points=points)
            answer.save()
    return render(request, 'quiz/upload.html', context={'quiz_id': quiz_id})

def upload(request):
    quiz_name = request.POST['quiz_name']
    quiz = Quiz(user_id=request.user.id, quiz_name=quiz_name, pub_date=timezone.now())
    quiz.save()

    question_number = int(request.POST['question_number'])

    for i in range(1, question_number+1):
        question_text = request.POST[f'question_text_{i}']
        question = Question(quiz_id=quiz.id, question_text=question_text)
        question.save()
        answer_number = request.POST[f'answer_{i}_number']
        for j in range(1, answer_number + 1):
            answer_text = request.POST[f'answer_text_{i}_{j}']
            given_points = request.POST[f'given_points_{i}_{j}']
            answer = Answer(question_id=question.id, answer_text=answer_text, points=given_points)
            answer.save()

    return render(request, 'quiz/upload.html', context={})

def delete(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    quiz.delete()
    return render(request, 'quiz/delete.html', context={})
