# Generated by Django 4.2.7 on 2023-11-12 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SocietiesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_prayer', models.CharField(max_length=300)),
                ('days', models.CharField(max_length=300)),
                ('prayer_download', models.FileField(null=True, upload_to='prayers')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocietiesApp.societies')),
            ],
        ),
    ]