# Generated by Django 4.0.6 on 2022-07-22 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='content',
        ),
    ]
