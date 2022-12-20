from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from myapp.admin import *
from django.utils import timezone
from django.core.paginator import Paginator
from myapp.forms import *
from django.contrib import messages
from django.urls import reverse
from django.db.models import Sum
from myappstaff.models import *

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
def user_detail(req, id):
    # if req.user.is_authenticated:
    #     cart = Add_Durable.objects.get_or_create(User = User, completed = False)
    product = Add_Durable.objects.get(id=id)
    context = {
        "name" : product.name,
        "category" : product.category,
        "status" : product.status,
        "quantity" : product.quantity,
        "description" : product.description,
        "image" : product.image,
        "id" : product.id,
        # "cart" : cart
    }
    return render(req,'pages/user_detail.html',context)

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

@login_required
def user_recommend_history(req):
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "page" : page,
    }
    return render(req, 'pages/user_recommend_history.html', context)     

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
        "AllRecList" : ListFromRec.objects.all(),
        "page" : page,
    }
    return render(req, 'pages/user_recommend.html', context)   

@login_required
def user_recommend_edit(req,id):
    obj = ListFromRec.objects.get(id=id)
    obj.name = req.POST['name']
    obj.brand = req.POST['brand']
    obj.quantity = req.POST['quantity']
    obj.price = req.POST['price']
    obj.link = req.POST['link']
    obj.description = req.POST['description']
    obj.datetime = timezone.now()
    obj.save()
    return redirect('/user_recommend') 

# รายงานสถานะข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
@login_required
def user_recommend_detail(req, id):
    AllRecList = ListFromRec.objects.filter(id=id).first()
    context = {
        "AllRecList" : AllRecList,
    }
    return render( req, 'pages/user_recommend_detail.html', context)

def deleteRecList(req, id):
    obj = ListFromRec.objects.get(id=id)
    obj.delete()
    return redirect('/user_recommend')