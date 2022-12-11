
from django import forms
from myappstaff.models import *
from django.forms import ModelForm


class All_CategoryTypeForm(ModelForm):
    class Meta:
        model = CategoryType
        fields = ['name_CategoryType']

class All_CategoryStatusForm(ModelForm):
    class Meta:
        model = CategoryStatus
        fields = ['name_CategoryStatus']     


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Add_Parcel
        fields = [ 'name', 'category', 'quantity', 'numdate', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'category': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'numdate': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-5'}),
            'image': forms.FileInput(attrs={'class': 'form-control rounded-pill'}),
        }
        labels = {
            'name' : 'Enter Product Name:',
            'category': 'Select Category: ',
            'quantity': 'Enter a quantity: ',
            'numdate': 'Enter a numdate: ',
            'description': 'Enter a Description: ',
            'image': 'Enter a image: ',
        }

class DurableForm(forms.ModelForm):
    class Meta:
        model = Add_Durable
        fields = [ 'name', 'category', 'quantity', 'numdate', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'category': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'numdate': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-5'}),
            'image': forms.FileInput(attrs={'class': 'form-control rounded-pill'}),
        }
        labels = {
            'name' : 'Enter Product Name:',
            'category': 'Select Category: ',
            'quantity': 'Enter a quantity: ',
            'numdate': 'Enter a numdate: ',
            'description': 'Enter a Description: ',
            'image': 'Enter a image: ',
        }