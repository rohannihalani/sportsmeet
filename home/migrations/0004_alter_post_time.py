# Generated by Django 4.0.6 on 2022-07-25 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_post_title_post_date_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
