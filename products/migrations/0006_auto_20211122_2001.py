# Generated by Django 3.2.9 on 2021-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211122_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='Products-img/', verbose_name='تصویر اول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='Products-img/', verbose_name='تصویر دوم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='Products-img/', verbose_name='تصویر سوم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='Products-img/', verbose_name='تصویر چهارم'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ar',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_en',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_fa',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_ku',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='نام محصول'),
        ),
    ]
