# Generated by Django 3.0.4 on 2020-05-17 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0020_delete_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('rate_id', models.AutoField(primary_key=True, serialize=False)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ManyToManyField(to='restapi.Question')),
                ('rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Rate')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Teacher')),
            ],
        ),
    ]
