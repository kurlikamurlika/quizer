from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('play/<int:quiz_id>/', views.play, name='play'),
    path('play/<int:quiz_id>/result/', views.result, name='result'),
    path('create/edit/', views.edit, name='edit'),
    path('create/upload/', views.upload, name='upload'),
    path('delete/<int:quiz_id>/', views.delete, name='delete'),
]