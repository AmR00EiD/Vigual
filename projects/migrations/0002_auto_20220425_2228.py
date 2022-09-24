# Generated by Django 3.2.13 on 2022-04-25 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_customuser_banckacc'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Freelancer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.freelancer'),
        ),
        migrations.AddField(
            model_name='projects',
            name='Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='Project',
            field=models.ImageField(default=None, upload_to='media/projects'),
        ),
    ]
