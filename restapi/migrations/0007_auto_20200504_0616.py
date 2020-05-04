# Generated by Django 3.0.4 on 2020-05-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ManyToManyField(to='restapi.Subject'),
        ),
    ]
