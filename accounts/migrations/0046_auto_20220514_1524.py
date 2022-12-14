# Generated by Django 3.2.13 on 2022-05-14 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20220514_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chats',
            name='user',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='massage',
            name='sender',
        ),
        migrations.AddField(
            model_name='chats',
            name='reciever',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chats',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
