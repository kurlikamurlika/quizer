from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text

class Play(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quiz.quiz_name}_{self.user.username}_{self.points}'

class Leaderboard(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    points = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quiz.quiz_name}_{self.user.username}_{self.points}'