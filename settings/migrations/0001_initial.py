# Generated by Django 3.2.9 on 2021-11-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('about_us', models.CharField(max_length=800)),
                ('about_us_small', models.CharField(max_length=600)),
                ('instagram', models.CharField(max_length=120)),
                ('whatsapp', models.CharField(max_length=120)),
                ('telegram', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
