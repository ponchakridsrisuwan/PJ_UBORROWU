from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.forms import ModelForm
from myappstaff.models import *
from django.utils import timezone

# ล็อคอิน
def staff_login(req):
    return render(req,'pages/staff_login.html')

class All_CategoryTypeForm(ModelForm):
    class Meta:
        model = CategoryType
        fields = ['name_CategoryType']
        
class All_CategoryMenuForm(ModelForm):
    class Meta:
        model = CategoryMenu
        fields = ['name_CategoryMenu']     

class All_CategoryDisplayForm(ModelForm):
    class Meta:
        model = CategoryDisplay
        fields = ['name_CategoryDisplay']
        
class All_CategoryStatusForm(ModelForm):
    class Meta:
        model = CategoryStatus
        fields = ['name_CategoryStatus']              

class All_PhoneForm(ModelForm):
    class Meta:
        model = Add_Phone
        fields = ['num_phone']                 

# การตั้งค่าหมวดหมุ่
def All_CategoryType(req):
    return render(req, 'pages/staff_setting.html', {
        'All_CategoryType': CategoryType.objects.all()
    })  

def Add_CategoryType(req):
    obj = CategoryType()
    obj.name_CategoryType = req.GET.get('name_CategoryType')
    obj.save()
    mydictionary = {
            "All_CategoryType": CategoryType.objects.all()
        }
    return render(req, 'pages/staff_setting.html', context=mydictionary)

def DeleteCategoryType(req,id):
    obj = CategoryType.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_CategoryType" : CategoryType.objects.all()
    }
    return render(req, 'pages/staff_setting.html', context=mydictionary)

# การตั้งค่ารายการ
def All_CategoryMenu(req):
    return render(req, 'pages/staff_setting_menu.html', {
        'All_CategoryMenu': CategoryMenu.objects.all()
    })  

def Add_CategoryMenu(req):
    obj = CategoryMenu()
    obj.name_CategoryMenu = req.GET.get('name_CategoryMenu')
    obj.save()
    mydictionary = {
            "All_CategoryMenu": CategoryMenu.objects.all()
        }
    return render(req, 'pages/staff_setting_menu.html', context=mydictionary)

def DeleteCategoryMenu(req,id):
    obj = CategoryMenu.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_CategoryMenu" : CategoryMenu.objects.all()
    }
    return render(req, 'pages/staff_setting_menu.html', context=mydictionary) 

# การตั้งค่าแสดงผล
def All_CategoryDisplay(req):
    return render(req, 'pages/staff_setting_display.html', {
        'All_CategoryDisplay': CategoryDisplay.objects.all()
    })  

def Add_CategoryDisplay(req):
    obj = CategoryDisplay()
    obj.name_CategoryDisplay = req.GET.get('name_CategoryDisplay')
    obj.save()
    mydictionary = {
            "All_CategoryDisplay": CategoryDisplay.objects.all()
        }
    return render(req, 'pages/staff_setting_display.html', context=mydictionary)

def DeleteCategoryDisplay(req,id):
    obj = CategoryDisplay.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_CategoryDisplay" : CategoryDisplay.objects.all()
    }
    return render(req, 'pages/staff_setting_display.html', context=mydictionary) 

# การตั้งค่าสถานะ
def All_CategoryStatus(req):
    return render(req, 'pages/staff_setting_status.html', {
        'All_CategoryStatus': CategoryStatus.objects.all()
    })  

def Add_CategoryStatus(req):
    obj = CategoryStatus()
    obj.name_CategoryStatus = req.GET.get('name_CategoryStatus')
    obj.save()
    mydictionary = {
            "All_CategoryStatus": CategoryStatus.objects.all()
        }
    return render(req, 'pages/staff_setting_status.html', context=mydictionary)

def DeleteCategoryStatus(req,id):
    obj = CategoryStatus.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "All_CategoryStatus" : CategoryStatus.objects.all()
    }
    return render(req, 'pages/staff_setting_status.html', context=mydictionary) 

# การแนะนำพัสดุเข้าสู่ระบบ    
def staff_introduction(req):
    return render(req, 'pages/staff_introduction.html', {
        'AllRecList': ListFromRec.objects.all()
    })  

# รายละเอียดการยืม
def staff_borrow_detail(req):
    return render(req,'pages/staff_borrow_detail.html')

# ประวัติการยืม
def staff_borrowing_history_detail(req):
    return render(req,'pages/staff_borrowing_history_detail.html')

# ข้อมูลการคืนพัสดุ-ครุภัณฑ์
def staff_borrowing_history(req):
    return render(req,'pages/staff_borrowing_history.html')

# จัดการรายการยืม
def staff_index_borrow(req):
    return render(req,'pages/staff_index_borrow.html')

# จัดการรายการยืม
def staff_index_borrownow(req):
    return render(req,'pages/staff_index_borrownow.html')

# จัดการรายการคืน
def staff_index_return(req):
    return render(req,'pages/staff_index_return.html')

# จัดการข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
def staff_introduction_detail(req):
    return render(req,'pages/staff_introduction_detail.html')

# ข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
def staff_introduction_hisdetail(req):
    return render(req,'pages/staff_introduction_hisdetail.html')

# รายละเอียดจัดการพัสดุ-ครุภัณฑ์
def staff_manage_detail(req):
    return render(req,'pages/staff_manage_detail.html')

# จัดการพัสดุ
def staff_manage_parcel(req):
    return render(req, 'pages/staff_manage_parcel.html', {
        'Add_Parcel': Add_Parcel.objects.all()
    })  

def staff_manage_parcel(req):
    parcel_category = CategoryType.objects.all()
    parcel_menu = CategoryMenu.objects.all()
    if req.method == 'POST':
        obj = Add_Parcel()
        obj.name = req.GET.get('name')
        obj.category = CategoryType.objects.get(id = req.GET.get('category'))
        obj.menu = CategoryMenu.objects.get(id = req.GET.get('menu'))
        obj.quantity = req.GET.get('quantity')
        obj.numdate = req.GET.get('numdate')
        obj.description = req.GET.get('description')
        obj.image = req.GET.get('image')
        obj.date = timezone.now()
        obj.save()

        return HttpResponseRedirect('/staff_manage_parcel')
    else:
        form = Add_Parcel()
        
    return render(req, 'pages/staff_manage_parcel.html', {'form': form, 'parcel_category':parcel_category,  'parcel_menu':parcel_menu})

def Deletestaff_manage_parcel(req,id):
    obj = Add_Parcel.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "staff_manage_parcel" : Add_Parcel.objects.all()
    }
    return render(req, 'pages/staff_manage_parcel.html', context=mydictionary)     

# จัดการครุภัณฑ์
def staff_manage_durable(req):
    return render(req, 'pages/staff_manage_parcel.html', {
        'staff_manage_durable': Add_Durable.objects.all()
    })  

def staff_manage_durable(req):
    durable_category = CategoryType.objects.all()
    durable_menu = CategoryMenu.objects.all()
    if req.method == 'POST':
        obj = Add_Durable()
        obj.name = req.GET.get('name')
        obj.category = CategoryType.objects.get(id = req.GET.get('category'))
        obj.menu = CategoryMenu.objects.get(id = req.GET.get('menu'))
        obj.quantity = req.GET.get('quantity')
        obj.numdate = req.GET.get('numdate')
        obj.description = req.GET.get('description')
        obj.image = req.GET.get('image')
        obj.date = timezone.now()
        obj.save()

        return HttpResponseRedirect('/staff_manage_durable')
    else:
        form = Add_Durable()
        
    return render(req, 'pages/staff_manage_durable.html', {'form': form, 'durable_category':durable_category,  'durable_menu':durable_menu})

def Deletestaff_manage_durable(req,id):
    obj = Add_Durable.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "staff_manage_durable" : Add_Durable.objects.all()
    }
    return render(req, 'pages/staff_manage_durable.html', context=mydictionary)    

# แก่ไขข้อมูลส่วนตัว และจัดการข้อมูลส่วนตัว
def staff_personal_info(req):
    return render(req, 'pages/staff_personal_info.html', {
        'All_Phone': Add_Phone.objects.all()
    })  

def staff_personal_info_edit(req):
    obj = Add_Phone()
    obj.num_phone = req.GET.get('num_phone')
    obj.save()
    mydictionary = {
            "All_Phone": Add_Phone.objects.all()
        }
    return render(req, 'pages/staff_personal_info_edit.html', context=mydictionary)

def staff_personal_info_edit(req):
    return render(req,'pages/staff_personal_info_edit.html')

def staff_personal_info(req):
    return render(req,'pages/staff_personal_info.html')

# รายละเอียดรายงานการยืมพัสดุ
def staff_report_borrowReport(req):
    return render(req,'pages/staff_report_borrowReport.html')

# รายงานจำนวนรายการพัสดุที่จำหน่ายทิ้ง
def staff_report_dispose(req):
    return render(req,'pages/staff_report_dispose.html')

# รายงานภาพรวมพัสดุ
def staff_report(req):
    return render(req,'pages/staff_report.html')

# รายงานจำนวนรายการพัสดุที่คงเหลือในระบบ
def staff_report_remaining(req):
    return render(req,'pages/staff_report_remaining.html')

# รายงานการยืมทั้งหมด
def staff_Including_borrowing(req):
    return render(req,'pages/staff_Including_borrowing.html')
