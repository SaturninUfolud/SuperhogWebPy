# Generated by Django 3.1.7 on 2021-02-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhog_app', '0002_articlesection_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='basic_description',
            field=models.TextField(default=''),
        ),
    ]
