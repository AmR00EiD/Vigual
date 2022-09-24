# Generated by Django 3.2.13 on 2022-05-02 22:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20220502_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_accounts_customuser_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
