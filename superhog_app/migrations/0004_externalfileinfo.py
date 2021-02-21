# Generated by Django 3.1.7 on 2021-02-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhog_app', '0003_article_basic_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalFileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetype', models.SmallIntegerField(choices=[(0, 'Picture'), (1, 'Video'), (2, 'Text'), (3, 'Source code'), (4, 'Other')], default=(0,))),
                ('description', models.CharField(default='', max_length=45)),
                ('internal_path', models.CharField(max_length=256)),
            ],
        ),
    ]
