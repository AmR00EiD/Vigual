# Generated by Django 3.2.13 on 2022-05-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(to='accounts.Follow'),
        ),
    ]
