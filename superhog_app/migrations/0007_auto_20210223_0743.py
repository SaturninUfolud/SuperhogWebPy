# Generated by Django 3.1.7 on 2021-02-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhog_app', '0006_auto_20210222_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='gallery',
            field=models.ManyToManyField(limit_choices_to={'available': True}, to='superhog_app.ExternalFileInfo'),
        ),
    ]