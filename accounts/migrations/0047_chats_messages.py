# Generated by Django 3.2.13 on 2022-05-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20220514_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='Messages',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Massage'),
        ),
    ]
