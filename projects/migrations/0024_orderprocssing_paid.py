# Generated by Django 3.2.13 on 2022-05-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_remove_finelorder_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderprocssing',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
