# Generated by Django 4.2.2 on 2023-06-08 20:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('elevator_id', models.IntegerField(primary_key=True, serialize=False)),
                ('current_floor', models.IntegerField(default=1)),
                ('direction', models.CharField(default='Stop', max_length=20)),
                ('is_running', models.BooleanField(default=False)),
                ('is_door_open', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=True)),
                ('is_operational', models.BooleanField(default=True)),
                ('requests', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='ElevatorSystem',
            fields=[
                ('elevatorsystem_id', models.AutoField(primary_key=True, serialize=False)),
                ('requests', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField(unique=True)),
            ],
        ),
    ]
