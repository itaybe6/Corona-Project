# Generated by Django 3.2.9 on 2021-11-28 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('phone_number', models.CharField(default=None, max_length=200, null=True)),
                ('password', models.CharField(default=None, max_length=200, null=True)),
                ('school', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(default=True, null=True)),
                ('my_class', models.CharField(default=None, max_length=200, null=True)),
                ('class_num', models.IntegerField(default=None, null=True)),
                ('phone_number', models.CharField(default=None, max_length=200, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
                ('user_id', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('phone_number', models.CharField(default=None, max_length=200, null=True)),
                ('password', models.CharField(default=None, max_length=200, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.manager')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
    ]