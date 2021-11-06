from django.db import models
from django_quill.fields import QuillField

class Image(models.Model):
	image = models.ImageField(upload_to="Products-img/", blank=True, null=True)

class Product(models.Model):
	name = models.CharField(max_length=80)
	description = QuillField()
	image = models.ManyToManyField(Image)
