# Generated by Django 4.2.3 on 2023-08-01 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_crud_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complited',
            new_name='completed',
        ),
    ]