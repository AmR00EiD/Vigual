# Generated by Django 3.2.13 on 2022-05-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_auto_20220514_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Massage'),
        ),
    ]