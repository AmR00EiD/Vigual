# Generated by Django 3.2.13 on 2022-05-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_remove_finelorder_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
