from typing import DefaultDict
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django_quill.fields import QuillField
from django.urls import reverse

from main.models import IPAddress

# translation
from django.utils.translation import gettext_lazy as _
from translated_fields import TranslatedField

class Category(models.Model):
	category = TranslatedField(models.CharField(max_length=60))
	
	def __str__(self):
		return self.category

class Product(models.Model):
	name = TranslatedField(models.CharField(verbose_name="" ,max_length=80, blank=True, null=True))
	category = models.ForeignKey(Category,verbose_name='دسته' ,blank=True, null=True, on_delete=models.CASCADE, related_name="cat")
	description = TranslatedField(QuillField(blank=True, null=True, verbose_name="توضیحات"))
	image1 = models.ImageField(upload_to="Products-img/", verbose_name="تصویر اول", blank=True, null=True)
	image2 = models.ImageField(upload_to="Products-img/", verbose_name="تصویر دوم", blank=True, null=True)
	image3 = models.ImageField(upload_to="Products-img/", verbose_name="تصویر سوم", blank=True, null=True)
	image4 = models.ImageField(upload_to="Products-img/", verbose_name="تصویر چهارم", blank=True, null=True)	
	hits = models.ManyToManyField(IPAddress, blank=True, related_name="hits")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("staff:staff_products")		
