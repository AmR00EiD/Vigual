# Generated by Django 3.2.13 on 2022-05-02 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_customuser_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='following',
        ),
    ]
