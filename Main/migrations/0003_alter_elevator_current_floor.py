# Generated by Django 4.2.2 on 2023-06-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_elevatorsystem_num_floors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='current_floor',
            field=models.IntegerField(default=0),
        ),
    ]
