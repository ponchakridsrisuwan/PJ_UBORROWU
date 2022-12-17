from myappSuper.models import *
from django.forms import ModelForm
from django import forms

class StaffForm(ModelForm):
    class Meta:
        model = Add_Staff_Email_User
        fields = ['email_staff']

class UserForm(ModelForm):
    class Meta:
        model = Add_User_Email_User
        fields = ['email_user']
        


#NEW DEW
class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Add_User
        fields = ['email_user', 'position', 'phone']
        widgets = {
            'email_user': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'position': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'phone': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
        }
        
        labels = {
            'Email' : 'กรอกEmail : ',
            'สถานะ': 'เลือกสถานะ :',
            'เบอร์โทรศัพท์': 'กรอกเบอร์โทรศัพท์ :',
        }