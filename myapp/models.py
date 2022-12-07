from django.db import models
from django.contrib.auth.models import User

class ListFromRec(models.Model):
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=300, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    datetime = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
