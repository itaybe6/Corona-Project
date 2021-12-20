# Generated by Django 3.2.9 on 2021-12-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211220_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(default=None, max_length=200, null=True)),
                ('pages', models.CharField(default=None, max_length=200, null=True)),
                ('remark', models.CharField(default=None, max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_ToDone', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
