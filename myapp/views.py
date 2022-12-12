from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from myapp.admin import *
from django.utils import timezone
from django.core.paginator import Paginator
from myapp.forms import *
from django.contrib import messages
from django.urls import reverse
from django.db.models import Sum

#หน้าหลัก
def HomePage(req):
    return render(req, 'pages/user_index.html' )

#หน้าลงทะเบียน
@login_required
def user_register(req):
    return render(req,'pages/register.html')

#หน้ายืม
@login_required
def user_borrow(req):
    return render(req,'pages/user_borrow.html')

#หน้าคืน
@login_required
def user_borrowed(req):
    return render(req,'pages/user_borrowed.html')

#หน้าประวัติ
@login_required
def user_history(req):
    return render(req,'pages/user_history.html')

#หน้ายืม
@login_required
def user_cart(req):
    return render(req,'pages/user_cart.html')    


#หน้ารายละเอียดพัสดุ
@login_required
def user_detail(req):
    return render(req,'pages/user_detail.html')

#หน้ารายการพัสดุ
def user_durable_articles(req):
    return render(req,'pages/user_durable_articles.html')

#หน้าจัดการแจ้งเตือน
@login_required
def user_notifications(req):
    return render(req,'pages/user_notifications.html')

#หน้าแก้ไขข้อมูลส่วนตัว
@login_required
def user_personal_info_edit(req):
    if req.method == "POST":
        username = req.user
        contact_user = req.POST.get('contact_user')
        obj = Contact(username=username, contact_user=contact_user)
        obj.save()
        return redirect('/user_personal_info')   
    else:
        obj = Contact()   
    obj = Contact.objects.all()    
    context = {
        "Contact": Contact.objects.all(),
    }
    return render(req, 'pages/user_personal_info_edit.html', context)    

"""def user_personal_info_edit(req,id):
    obj = Contact.objects.get(id=id)
    obj.contact_user = req.POST['contact_user']
    obj.save()
    return redirect('/user_personal_info_edit')"""

#หน้าข้อมูลส่วนตัว
@login_required
def user_personal_info(req):
    return render(req, 'pages/user_personal_info.html')     
      

#หน้าแนะนำพัสดุ
@login_required
def user_recommend(req):
    if req.method == "POST":
        username = req.user
        name = req.POST.get('name')
        brand = req.POST.get('brand')
        quantity = req.POST.get('quantity')
        price = req.POST.get('price')
        link = req.POST.get('link')
        description = req.POST.get('description')
        datetime = timezone.now()
        obj = ListFromRec(username=username, name=name, brand=brand, quantity=quantity, 
                          price=price, link=link, description=description, datetime=datetime)
        obj.save()
        return redirect('/user_recommend')   
    else:
        obj = ListFromRec()   
    obj = ListFromRec.objects.all()   
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "AllRecList": ListFromRec.objects.all(),
        "page" : page,
    }
    return render(req, 'pages/user_recommend.html', context)    

def deleteRecList(req, id):
    obj = ListFromRec.objects.get(id=id)
    obj.delete()
    return redirect('/user_recommend')