# Generated by Django 3.1.1 on 2020-09-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0036_auto_20200920_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
