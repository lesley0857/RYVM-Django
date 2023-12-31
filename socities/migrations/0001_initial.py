# Generated by Django 3.2.23 on 2023-11-26 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Societies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Society_name', models.CharField(default='Society Name', max_length=300)),
                ('Venue', models.CharField(default='Church Compound', max_length=300)),
                ('Days_of_meeting', models.CharField(default='Sunday', max_length=300)),
                ('profile_pic', models.ImageField(default='/Koala.jpg/', upload_to='')),
            ],
        ),
    ]
