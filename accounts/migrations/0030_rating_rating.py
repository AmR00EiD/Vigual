# Generated by Django 3.2.13 on 2022-05-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20220508_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]