# Generated by Django 3.2.13 on 2022-05-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0057_rename_sub_rateprofile_submit'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rate',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.rateprofile'),
        ),
    ]