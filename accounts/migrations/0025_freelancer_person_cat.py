# Generated by Django 3.2.13 on 2022-05-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_customuser_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='person_cat',
            field=models.CharField(blank=True, choices=[('مصمم ديكور', 'مصمم ديكور'), ('مصمم ديكور تصميم داخلي', 'مصمم ديكور تصميم داخلي'), ('مصمم ديكور تصميم خارجي', 'مصمم ديكور تصميم خارجي')], max_length=50),
        ),
    ]