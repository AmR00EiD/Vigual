# Generated by Django 3.2.13 on 2022-04-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_skills'),
        ('accounts', '0018_auto_20220427_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='cat',
            field=models.ManyToManyField(blank=True, default='null', to='projects.Category'),
        ),
    ]
