# Generated by Django 3.0.7 on 2020-06-30 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_coll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_anotherName_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_director_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_grade_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_language_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_mainRole_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_scenarist_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_title_str',
        ),
        migrations.RemoveField(
            model_name='tablefilm',
            name='fl_type_str',
        ),
    ]