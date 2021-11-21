from django.db import models
from extensions.utils import jalali_converter

class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    text = models.TextField()
    created_on = models.DateField(blank=True, null=True ,auto_now_add=True)
    created_on_time = models.TimeField(blank=True, null=True ,auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.phone_number}"

    def jcreated_on(self):
        return jalali_converter(self.created_on)    
        
class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
    created_on = models.DateTimeField(blank=True, null=True ,auto_now_add=True)
    
    def __str__(self):
        return self.ip_address        