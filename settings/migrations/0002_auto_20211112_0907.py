# Generated by Django 3.2.9 on 2021-11-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='about_us',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='about_us_small',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='title',
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_ar',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='about_us'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_en',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='about_us'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_fa',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='about_us'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_ku',
            field=models.CharField(blank=True, max_length=800, null=True, verbose_name='about_us'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_small_ar',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='about_us_small'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_small_en',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='about_us_small'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_small_fa',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='about_us_small'),
        ),
        migrations.AddField(
            model_name='setting',
            name='about_us_small_ku',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='about_us_small'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_ar',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_en',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_fa',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='setting',
            name='title_ku',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='title'),
        ),
    ]