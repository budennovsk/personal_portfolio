# Generated by Django 4.0.6 on 2022-09-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted_alter_todo_important'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(help_text='Enter field documentation', max_length=100),
        ),
    ]