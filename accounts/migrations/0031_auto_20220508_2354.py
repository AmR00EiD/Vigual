# Generated by Django 3.2.13 on 2022-05-08 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_rating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='freelancer',
            name='skills',
        ),
    ]