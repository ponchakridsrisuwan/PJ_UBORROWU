from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from myappSuper.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def admin_detail(req):
    return render(req, "pages/admin_detail.html")

@login_required
def admin_staff(req):
    return render(req, "pages/admin_staff.html")

@login_required
def admin_user(req):
    return render(req, "pages/admin_user.html")

@login_required
def admin_staff_setting(req):
    if req.method == "POST":
        email_staff = req.POST.get('email_staff')
        obj = Add_Staff_Email_User(email_staff=email_staff)
        obj.save()
        return redirect('/admin_staff_setting')   
    else:
        obj = Add_Staff_Email_User()   
    obj = Add_Staff_Email_User.objects.all()   
    AllStaff = Add_Staff_Email_User.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllStaff, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "AllStaff": Add_Staff_Email_User.objects.all(),
        "page" : page,
    }
    return render(req, 'pages/admin_staff_setting.html', context)   

@login_required
def deleteStaff(req, id):
    obj = Add_Staff_Email_User.objects.get(id=id)
    obj.delete()
    return redirect('/admin_staff_setting')

@login_required
def admin_user_setting(req):
    if req.method == "POST":
        email_user = req.POST.get('email_user')
        obj = Add_User_Email_User(email_user=email_user)
        obj.save()
        return redirect('/admin_user_setting')   
    else:
        obj = Add_User_Email_User()   
    obj = Add_User_Email_User.objects.all()   
    AllUser = Add_User_Email_User.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllUser, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "AllUser": Add_User_Email_User.objects.all(),
        "page" : page,
    }
    return render(req, 'pages/admin_user_setting.html', context)   

@login_required
def deleteUser(req, id):
    obj = Add_User_Email_User.objects.get(id=id)
    obj.delete()
    return redirect('/admin_user_setting') 

@login_required
def SearchStaff(req):
    q = req.GET['query']
    context = {
        "All_staff" : Add_Staff_Email_User.objects.filter(title__contains=q)
    }
    return render(req,'pages/admin_staff_setting.html',context)

@login_required
def SearchUser(req):
    q = req.GET['query']
    context = {
        "All_user" : Add_User_Email_User.objects.filter(title__contains=q)
    }
    return render(req,'pages/admin_user_setting.html',context)