# Generated by Django 3.0.7 on 2020-06-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_auto_20200630_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmdata',
            name='fl_commentNum_int',
            field=models.IntegerField(default='', null=0),
        ),
        migrations.AlterField(
            model_name='filmdata',
            name='fl_grade_str',
            field=models.FloatField(default='', null=0),
        ),
        migrations.AlterField(
            model_name='filmdata',
            name='fl_replyNum_int',
            field=models.IntegerField(default='', null=0),
        ),
    ]