# Generated by Django 3.2.13 on 2022-08-18 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='name',
            new_name='nickname',
        ),
    ]
