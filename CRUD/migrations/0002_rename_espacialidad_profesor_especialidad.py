# Generated by Django 5.1.1 on 2024-12-17 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='espacialidad',
            new_name='especialidad',
        ),
    ]