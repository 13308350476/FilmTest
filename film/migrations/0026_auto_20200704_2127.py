# Generated by Django 3.0.7 on 2020-07-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0025_auto_20200704_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
