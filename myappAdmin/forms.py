from myappAdmin.models import *
from django.forms import ModelForm

class StaffForm(ModelForm):
    class Meta:
        model = Add_Staff
        fields = ['email_staff']

##########
class StaffForm(ModelForm):
    class Meta:
        model = Add_mystaff
        fields = ['email_staff']

class UserForm(ModelForm):
    class Meta:
        model = Add_User
        fields = ['email_user']
        