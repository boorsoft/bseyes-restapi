# Generated by Django 3.0.4 on 2020-05-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0011_auto_20200516_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Subject'),
        ),
        migrations.AddField(
            model_name='answer',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restapi.Teacher'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
