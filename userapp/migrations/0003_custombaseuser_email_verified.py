# Generated by Django 3.2.23 on 2023-11-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_remove_usersocities_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='custombaseuser',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
