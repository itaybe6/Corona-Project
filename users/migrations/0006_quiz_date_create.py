# Generated by Django 3.2.9 on 2021-12-24 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_student_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
