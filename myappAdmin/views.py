from django.shortcuts import render
from myappAdmin.models import *
from django.forms import ModelForm


def admin_detail(req):
    return render(req, "pages/admin_detail.html")

def admin_login(req):
    return render(req,'pages/admin_login.html')

def admin_admin(req):
    return render(req,'pages/admin_admin.html')

class StaffForm(ModelForm):
    class Meta:
        model = Add_Staff
        fields = ['email_staff']

class UserForm(ModelForm):
    class Meta:
        model = Add_User
        fields = ['email_user']

def All_staff(req):
    return render(req, 'pages/admin_staff.html', {
        'All_staff': Add_Staff.objects.all()
    })    

def All_user(req):
    return render(req, 'pages/admin_user.html', {
        'All_user': Add_User.objects.all()
    })  

def Add_staff(req):
    obj = Add_Staff()
    obj.email_staff = req.GET.get('email_staff')
    obj.save()
    mydictionary = {
            "All_staff": Add_Staff.objects.all()
        }
    return render(req, 'pages/admin_staff_setting.html', context=mydictionary)

def Add_user(req):
    obj = Add_User()
    obj.email_user = req.GET.get('email_user')
    obj.save()
    mydictionary = {
            "All_user": Add_User.objects.all()
        }
    return render(req, 'pages/admin_user_setting.html', context=mydictionary)

def SearchStaff(req):
    q = req.GET['query']
    mydictionary = {
        "All_staff" : Add_Staff.objects.filter(title__contains=q)
    }
    return render(req,'pages/admin_staff_setting.html',context=mydictionary)

def SearchUser(req):
    q = req.GET['query']
    mydictionary = {
        "All_user" : Add_User.objects.filter(title__contains=q)
    }
    return render(req,'pages/admin_user_setting.html',context=mydictionary)

def DeleteStaff(req,id):
    obj = Add_Staff.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_staff" : Add_Staff.objects.all()
    }
    return render(req, 'pages/admin_staff_setting.html', context=mydictionary)

def DeleteUser(req,id):
    obj = Add_User.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_user" : Add_User.objects.all()
    }
    return render(req, 'pages/admin_user_setting.html', context=mydictionary)