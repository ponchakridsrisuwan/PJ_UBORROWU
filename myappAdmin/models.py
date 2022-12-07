from django.db import models

class Add_Staff(models.Model):
    email_staff = models.EmailField(primary_key=bool, max_length=254)

    def __str__(self):
        return self.email_staff
    
class Add_User(models.Model):
    email_user = models.EmailField(primary_key=bool, max_length=254)

    def __str__(self):
        return self.email_user
