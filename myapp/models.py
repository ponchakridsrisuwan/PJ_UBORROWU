from django.db import models
from django.contrib.auth.models import User

class ListFromRec(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, null=True)
    brand = models.CharField(max_length=300, null=True)
    quantity = models.IntegerField(default=1, null=True)
    price = models.FloatField(default=0.0, null=True)
    link = models.URLField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)
    datetime = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    contact_user = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.contact_user