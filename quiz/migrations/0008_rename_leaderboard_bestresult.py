# Generated by Django 4.0 on 2022-03-18 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('quiz', '0007_alter_answer_question_alter_leaderboard_quiz_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leaderboard',
            new_name='BestResult',
        ),
    ]