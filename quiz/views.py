from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Quiz, Question, Answer, Play, BestResult
from django.utils import timezone
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Sum
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


class ProfileView(generic.DetailView):
    model = User
    template_name = 'quiz/profile.html'
    context_object_name = 'profile'

class AboutView(generic.TemplateView):
    template_name = 'quiz/about_us.html'

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
    question_list = quiz.questions.all()
    return render(request, 'quiz/play.html', context={"quiz": quiz, "question_list": question_list})


def result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    points = 0
    question_list = quiz.questions.all()

    for question in question_list:
        selected_answer = question.answers.get(pk=request.POST[f'answer{question.id}'])
        points += selected_answer.points

    play = Play(quiz_id=quiz.id, points=points, user_id=request.user.id)
    play.save()
    try:
        best_result = BestResult.objects.get(quiz_id=quiz.id, user_id=request.user.id)
        print(best_result)
        if best_result.points < points:
            best_result.points = points
            best_result.save()
    except:
        best_result_create = BestResult(quiz_id=quiz.id, user_id=request.user.id, points=points)
        best_result_create.save()

    return render(request, 'quiz/result.html', context={'points': points, 'quiz': quiz,})


class CreateView(generic.TemplateView):
    template_name = 'quiz/create.html'

def upload(request):
    quiz_name = request.POST[f'quiz_name']
    quiz = Quiz(user_id=request.user.id, quiz_name=quiz_name, pub_date=timezone.now())
    quiz.save()
    question_number = int(request.POST['question_number'])
    for i in range(1, question_number+1):
        question_text = request.POST[f'question_text_{i}']
        question = Question(quiz_id=quiz.id, question_text=question_text)
        question.save()
        answer_number = int(request.POST[f'answer_{i}_number'])
        for j in range(1, answer_number+1):
            answer_text = request.POST[f'answer_text_{i}_{j}']
            points = request.POST[f'given_points_{i}_{j}']
            answer = Answer(question_id=question.id, answer_text=answer_text, points=points)
            answer.save()
    return render(request, 'quiz/upload.html', context={'quiz_id': quiz.id})

def delete(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    quiz.delete()
    return render(request, 'quiz/delete.html', context={})

def leaderboard(request):
    user_list = User.objects.all()
    leaderboard = [[]]
    for profile in user_list:
        if len(profile.best_results.all()) > 0:
            total_points = profile.best_results.aggregate(Sum('points'))
            leaderboard.append([profile, total_points['points__sum']])
    leaderboard = leaderboard[1:]
    leaderboard.sort(key=lambda row: (row[1]), reverse=True)
    leaderboard_dict = {
        'leaderboard': leaderboard
    }
    return render(request, 'quiz/leaderboard.html', context=leaderboard_dict)