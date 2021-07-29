# Generated by Django 3.2.5 on 2021-07-29 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10000)),
                ('user', models.CharField(max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 29, 9, 57, 10, 43854))),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]
