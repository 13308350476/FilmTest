# Generated by Django 3.0.7 on 2020-07-04 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0023_auto_20200704_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='c_film_title',
        ),
    ]
