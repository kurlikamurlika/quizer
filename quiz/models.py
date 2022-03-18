from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizes')
    quiz_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text

class Play(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='plays')
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plays')

    def __str__(self):
        return f'{self.quiz.quiz_name}_{self.user.username}_{self.points}'

class BestResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='best_results')
    points = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='best_results')

    def __str__(self):
        return f'{self.quiz.quiz_name}_{self.user.username}_{self.points}'