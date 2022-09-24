# Generated by Django 3.2.13 on 2022-05-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_freelancer_person_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='person_cat',
            field=models.CharField(blank=True, choices=[('مصمم ديكور', 'مصمم ديكور'), ('مصمم ديكور تصميم داخلي', 'مصمم ديكور تصميم داخلي'), ('مصمم ديكور تصميم خارجي', 'مصمم ديكور تصميم خارجي'), ('مصمم جرافيم', 'مصمم جرافيك'), ('UIUX مصمم جرافيك', 'UIUX مصمم جرافيك'), ('مصمم لوجو جرافيك', 'مصمم لوجو جرافيك'), ('مصمم جرافيك براندينج', 'مصمم جرافيك براندينج'), ('مصمم جرافيك بوستات سوشيال ميديا', 'مصمم جرافيك بوستات سوشيال ميديا'), ('مصمم مواشن جرافيك', 'مصمم مواشن جرافيك'), ('مصمم موشن جرافيك انيميشن', 'مصمم موشن جرافيك انيميشن')], max_length=50),
        ),
    ]
