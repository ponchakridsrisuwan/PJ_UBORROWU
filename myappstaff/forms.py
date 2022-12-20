
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
        
"""class Status_recForm(ModelForm):
    class Meta:
        model = Status_rec
        fields = ['status']  """                


class ParcelForm(forms.ModelForm):
    class Meta:
        model = Add_Parcel
        fields = [ 'name', 'category', 'status', 'quantity', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'category': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'status': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-5'}),
            'image': forms.FileInput(attrs={'class': 'form-control rounded-pill'}),
        }
        labels = {
            'name' : 'ระบุชื่อพัสดุ :',
            'category': 'เลือกหมวดหมู่พัสดุ :',
            'status': 'เลือกสถานะพัสดุ :',
            'quantity': 'ระบุจำนวนพัสดุ :',
            'description': 'รายละเอียดพัสดุ :',
            'image': 'แนบไฟล์ภาพพัสดุ :',
        }

class DurableForm(forms.ModelForm):
    class Meta:
        model = Add_Durable
        fields = [ 'name', 'category', 'quantity', 'numdate', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'category': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'status': forms.Select(attrs={'class': 'form-control rounded-pill'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'numdate': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-5'}),
            'image': forms.FileInput(attrs={'class': 'form-control rounded-pill'}),
        }
        
        labels = {
            'name' : 'ระบุชื่อครุภัณฑ์ :',
            'category': 'เลือกหมวดหมู่ครุภัณฑ์ :',
            'status': 'เลือกสถานะครุภัณฑ์ :',
            'quantity': 'ระบุจำนวนครุภัณฑ์ :',
            'numdate': 'ระบุจำนวนวันที่อนุญาตให้ยืม :',
            'description': 'รายละเอียดครุภัณฑ์ :',
            'image': 'แนบไฟล์ภาพครุภัณฑ์ :',
        }