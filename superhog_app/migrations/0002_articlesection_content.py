# Generated by Django 3.1.7 on 2021-02-20 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesection',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
