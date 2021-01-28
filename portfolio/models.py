from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    topic = models.CharField(max_length=30)
    message = models.CharField(max_length=3000)
