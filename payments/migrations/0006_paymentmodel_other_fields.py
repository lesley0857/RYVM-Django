# Generated by Django 4.2.7 on 2023-12-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_alter_paymentmodel_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmodel',
            name='other_fields',
            field=models.TextField(blank=True),
        ),
    ]