# Generated by Django 3.0.4 on 2020-05-04 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0007_auto_20200504_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student',
        ),
    ]