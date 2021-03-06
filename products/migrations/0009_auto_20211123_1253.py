# Generated by Django 3.2.9 on 2021-11-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211122_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_ar',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_fa',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_ku',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ar',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_fa',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ku',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name=''),
        ),
    ]
