# Generated by Django 3.0.6 on 2020-05-22 15:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0029_auto_20200522_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 15, 39, 16, 257728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 15, 39, 16, 256420, tzinfo=utc)),
        ),
    ]
