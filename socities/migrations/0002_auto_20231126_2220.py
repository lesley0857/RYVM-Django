# Generated by Django 3.2.23 on 2023-11-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='societies',
            name='alternative_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='societies',
            name='contact_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
