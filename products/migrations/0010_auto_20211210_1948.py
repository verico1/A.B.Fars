# Generated by Django 3.2.9 on 2021-12-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211123_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_ar',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_fa',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ku',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='name'),
        ),
    ]
