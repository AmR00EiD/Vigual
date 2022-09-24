# Generated by Django 3.2.13 on 2022-05-08 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_customuser_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rating',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.rating'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to=settings.AUTH_USER_MODEL),
        ),
    ]
