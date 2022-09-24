# Generated by Django 3.2.13 on 2022-04-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_skills'),
        ('accounts', '0010_alter_customuser_banckacc'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='skills',
            field=models.ManyToManyField(default='null', to='projects.skills'),
        ),
    ]
