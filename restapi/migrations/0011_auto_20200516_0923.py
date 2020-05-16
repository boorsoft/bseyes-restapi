# Generated by Django 3.0.4 on 2020-05-16 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0010_auto_20200512_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comment',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Question'),
        ),
    ]
