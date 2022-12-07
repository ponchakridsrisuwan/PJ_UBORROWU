from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import ListFromRec
from django.forms import ModelForm
from django.utils import timezone

#def index(req):
    #message="id:%s, uasername:%s firstname:%s, lastname:%s"%(req.user.pk, req.user.username, req.user.first_name, req.user.last_name)
    #html = "<p>%s</p>" % (message)
    #return HttpResponse(html)

#หน้าหลัก
def HomePage(req):
    return render(req, 'pages/user_index.html' )

#หน้าลงทะเบียน
def user_register(req):
    return render(req,'pages/register.html')

#หน้ายืม
def user_borrow(req):
    return render(req,'pages/user_borrow.html')

#หน้าคืน
def user_borrowed(req):
    return render(req,'pages/user_borrowed.html')

#หน้าประวัติ
def user_history(req):
    return render(req,'pages/user_history.html')

#หน้ารายละเอียดการทำการคืน
def user_return_parcel_detail(req):
    return render(req,'pages/user_return_parcel_detail.html')

#หน้ายืม
def user_cart(req):
    return render(req,'pages/user_cart.html')    

#หน้ารายละเอียดการทำรายการ
def user_cart_detail_del(req):
    return render(req,'pages/user_cart_detail_del.html')

#หน้ารายละเอียดพัสดุ
def user_detail(req):
    return render(req,'pages/user_detail.html')

#หน้ารายการพัสดุ
def user_durable_articles(req):
    return render(req,'pages/user_durable_articles.html')

#หน้าจัดการแจ้งเตือน
def user_notifications(req):
    return render(req,'pages/user_notifications.html')

#หน้าแก้ไขข้อมูลส่วนตัว
def user_personal_info_edit(req):
    return render(req,'pages/user_personal_info_edit.html')

#หน้าข้อมูลส่วนตัว
def user_personal_info(req):
    return render(req,'pages/user_personal_info.html')

#หน้าแนะนำพัสดุ
class ListRecForm(ModelForm):
    class Meta:
        model = ListFromRec
        fields = ['name', 'brand', 'quantity','price', "link", 'description']

def AllRecList(req):
    return render(req, 'pages/user_recommend.html', {
        'AllRecList': ListFromRec.objects.all()
    })

def user_recommend(req):
    obj = ListFromRec()
    obj.username = req.user
    obj.name = req.GET.get('name')
    obj.brand = req.GET.get('brand')
    obj.quantity = req.GET.get('quantity')
    obj.price = req.GET.get('price')
    obj.link = req.GET.get('link')
    obj.description = req.GET.get('description')
    obj.datetime = timezone.now()
    obj.save()
    mydictionary = {
            "AllRecList": ListFromRec.objects.all()
        }
    return render(req, 'pages/user_recommend.html', context=mydictionary)

"""def deleteRecList(req, id):
    obj = ListFromRec.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "AllRecList" : ListFromRec.objects.all()
    }
    return render(req, 'pages/user_recommend.html', context=mydictionary)"""

def deleteRecList(request, pk):
	queryset = ListFromRec.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/user_recommend')
	return render(request, 'pages/user_recommend.html')
