# Generated by Django 3.2.13 on 2022-05-14 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20220513_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='massage',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='massage',
            name='author',
        ),
    ]
