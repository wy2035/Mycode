# Generated by Django 2.1.5 on 2019-02-10 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
