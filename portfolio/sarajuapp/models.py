from django.db import models

# Create your models here.
class Connection(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)

    time = models.CharField(max_length=150)
    device_type = models.CharField(max_length=250)
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    location = models.CharField(max_length=500)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name} / {self.email} / {self.phone} / {self.ip}"

class Viewed(models.Model):
    time = models.CharField(max_length=150)
    device_type = models.CharField(max_length=250)
    os = models.CharField(max_length=50)
    browser = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    location = models.CharField(max_length=500)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.ip} / {self.device_type} / {self.browser} / {self.os}"
