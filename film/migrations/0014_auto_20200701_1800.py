# Generated by Django 3.0.7 on 2020-07-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0013_filmtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmtag',
            name='ft_title',
            field=models.TextField(unique=True),
        ),
    ]
