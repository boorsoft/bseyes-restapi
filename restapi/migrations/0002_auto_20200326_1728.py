# Generated by Django 3.0.4 on 2020-03-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_body', models.CharField(max_length=300)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Quesion',
        ),
    ]
