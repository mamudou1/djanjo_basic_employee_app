# Generated by Django 4.2.6 on 2023-10-18 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emplyee',
            new_name='Employee',
        ),
    ]
