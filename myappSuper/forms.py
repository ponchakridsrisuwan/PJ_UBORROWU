from myappSuper.models import *
from django.forms import ModelForm

class StaffForm(ModelForm):
    class Meta:
        model = Add_Staff_Email_User
        fields = ['email_staff']

class UserForm(ModelForm):
    class Meta:
        model = Add_User_Email_User
        fields = ['email_user']
        