from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('register/', views.register, name='register'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('play/<int:quiz_id>/', views.play, name='play'),
    path('play/<int:quiz_id>/result/', views.result, name='result'),
    path('create/upload/', views.upload, name='upload'),
    path('delete/<int:quiz_id>/', views.delete, name='delete'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]