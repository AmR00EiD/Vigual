# Generated by Django 3.2.13 on 2022-05-09 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20220510_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='ord_det',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.orderprocssing'),
        ),
    ]
