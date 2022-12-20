from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from myapp.models import *


class CategoryType(models.Model):
    name_CategoryType = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_CategoryType     

class CategoryStatus(models.Model):
    name_CategoryStatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name_CategoryStatus            


class Add_Parcel(models.Model):
    # id
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE, null=True, related_name="category_parcel")
    status = models.ForeignKey(CategoryStatus, on_delete=models.CASCADE, null=True, related_name="status_parcel")
    quantity = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Parcel')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Add_Durable(models.Model):
    # id
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE, null=True, related_name="category_durable")
    status = models.ForeignKey(CategoryStatus, on_delete=models.CASCADE, null=True, related_name="status_durable")
    quantity = models.CharField(max_length=200, null=True, blank=True)
    numdate = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Durable')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    