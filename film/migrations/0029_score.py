# Generated by Django 3.0.7 on 2020-07-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0028_auto_20200705_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_score_str', models.CharField(default='5.6', max_length=32)),
                ('s_user_name', models.CharField(default='01', max_length=128)),
                ('s_film_title', models.CharField(default='坏孩子的秋天', max_length=128)),
                ('score_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
