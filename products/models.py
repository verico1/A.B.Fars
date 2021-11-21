from typing import DefaultDict
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django_quill.fields import QuillField

from main.models import IPAddress

# translation
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

class Image(models.Model):
	image = models.ImageField(upload_to="Products-img/", blank=True, null=True)	

class Category(models.Model):
	category = TranslatedField(models.CharField(max_length=60))

class Product(models.Model):
	name = TranslatedField(models.CharField(max_length=80, blank=True, null=True))
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="cat")
	description = TranslatedField(QuillField())
	image = models.ManyToManyField(Image)
	hits = models.ManyToManyField(IPAddress, blank=True, related_name="hits")
