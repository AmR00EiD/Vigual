# Generated by Django 3.2.13 on 2022-05-07 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_freelancer_person_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
