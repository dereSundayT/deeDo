# Generated by Django 3.0.8 on 2020-07-31 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todolevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todos.TodoLevel'),
        ),
    ]