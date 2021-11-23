from django.db import models

# translation
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

class Setting(models.Model):
    title = TranslatedField(models.CharField(max_length=120, blank=True, null=True))
    meta_title = TranslatedField(models.CharField(max_length=120, blank=True, null=True))
    about_us = TranslatedField(models.CharField(max_length=800, blank=True, null=True))
    about_us_small = TranslatedField(models.CharField(max_length=600, blank=True, null=True))
    address = TranslatedField(models.CharField(max_length=600, blank=True, null=True))
    
    instagram = models.CharField(max_length=120)
    whatsapp = models.CharField(max_length=120)
    telegram =models.CharField(max_length=120)
    email = models.EmailField()

    products_count = models.PositiveIntegerField(default=0)
    international_customers = models.PositiveIntegerField(default=0)
    years_of_activity = models.PositiveIntegerField(default=0)
    domestic_customers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'تنظیمات'
        