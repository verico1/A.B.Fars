from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=11)
    text = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.phone_number}"
        