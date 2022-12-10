from django.db import models

class Add_Staff_Email_User(models.Model):
    email_staff = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.email_staff
    
class Add_User_Email_User(models.Model):
    email_user = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.email_user
