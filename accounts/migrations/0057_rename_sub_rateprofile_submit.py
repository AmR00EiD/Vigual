# Generated by Django 3.2.13 on 2022-05-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_rateprofile_sub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rateprofile',
            old_name='sub',
            new_name='submit',
        ),
    ]
