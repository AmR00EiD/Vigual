# Generated by Django 3.2.13 on 2022-05-06 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_customuser_following'),
        ('projects', '0005_auto_20220506_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=8, null=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('post', models.ManyToManyField(blank=True, default='null', to='projects.Post')),
                ('usercomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.freelancer')),
            ],
        ),
    ]
