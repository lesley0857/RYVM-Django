# Generated by Django 3.2.23 on 2023-11-26 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersocities',
            name='position',
        ),
    ]
