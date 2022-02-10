from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
class User(models.Model):
    first_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=200)
    user_image = models.ImageField(upload_to=f'user_images/{username}/')
    reg_date = models.DateTimeField('Дата регистрации')

    def __str__(self):
        return self.user_email
'''

class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=200)

    '''
    def getUsername(self):
        return self.user.username
    username = getUsername
    quiz_image = models.ImageField(upload_to=f'user_images/{username}/{quiz_name}/')
    '''

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
    user = models.ForeignKey(User, on_delete=models. CASCADE)

    def __str__(self):
        return f'{self.quiz.quiz_name}_{self.user.username}_{self.points}'