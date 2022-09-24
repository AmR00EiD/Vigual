# Generated by Django 3.2.13 on 2022-05-06 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_orderprocssing'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinelOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oredrp', models.ImageField(default=None, upload_to='media/orders', verbose_name='order')),
                ('rate', models.FloatField(max_length=2)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.orderprocssing', verbose_name='orderdetalis')),
            ],
        ),
    ]