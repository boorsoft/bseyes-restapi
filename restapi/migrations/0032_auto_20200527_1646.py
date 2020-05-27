# Generated by Django 3.0.6 on 2020-05-27 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0031_merge_20200527_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='rate',
        ),
        migrations.AddField(
            model_name='answer',
            name='rate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]