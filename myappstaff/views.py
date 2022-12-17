from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib.auth.decorators import login_required
from myappstaff.forms import *
from django.utils import timezone
from django.core.paginator import Paginator
from myappstaff.models import *

# การตั้งค่าหมวดหมุ่
@login_required
def staff_setting(req):
    if req.method == "POST":
        name_CategoryType = req.POST.get('name_CategoryType')
        obj = CategoryType(name_CategoryType=name_CategoryType)
        obj.save()
        return redirect('/staff_setting')   
    else:
        obj = CategoryType()   
    obj = CategoryType.objects.all()   
    AllCategoryType = CategoryType.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllCategoryType, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "All_CategoryType": CategoryType.objects.all(),
        "page" : page
    }
    return render(req, 'pages/staff_setting.html', context)    

@login_required
def deleteCategoryType(req, id):
    obj = CategoryType.objects.get(id=id)
    obj.delete()
    return redirect('/staff_setting')

@login_required
def edit_staff_setting(req,id):
    obj = CategoryType.objects.get(id=id)
    obj.name_CategoryType = req.POST['name_CategoryType']
    obj.save()
    return redirect('/staff_setting')
    

# การตั้งค่าสถานะ
@login_required
def staff_setting_status(req):
    if req.method == "POST":
        name_CategoryStatus = req.POST.get('name_CategoryStatus')
        obj = CategoryStatus(name_CategoryStatus=name_CategoryStatus)
        obj.save()
        return redirect('/staff_setting_status')   
    else:
        obj = CategoryStatus()   
    obj = CategoryStatus.objects.all()   
    AllCategoryStatus = CategoryStatus.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllCategoryStatus, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "All_CategoryStatus": CategoryStatus.objects.all(),
        "page" : page
    }
    return render(req, 'pages/staff_setting_status.html', context)    

@login_required
def DeleteCategoryStatus(req, id):
    obj = CategoryStatus.objects.get(id=id)
    obj.delete()
    return redirect('/staff_setting_status')

@login_required
def edit_staff_setting_status(req,id):
    obj = CategoryStatus.objects.get(id=id)
    obj.name_CategoryStatus = req.POST['name_CategoryStatus']
    obj.save()
    return redirect('/staff_setting_status')

# การแนะนำพัสดุเข้าสู่ระบบ    
@login_required
def staff_introduction(req):
    AllRecList = ListFromRec.objects.all()
    AllRecList_count = AllRecList.count()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page,
        "AllRecList_count" : AllRecList_count
    }
    return render( req, 'pages/staff_introduction.html', context)

@login_required
def staff_introduction_history(req):
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page
    }
    return render( req, 'pages/staff_introduction_history.html', context)

# รายละเอียดการยืม
@login_required
def staff_borrow_detail(req):
    return render(req,'pages/staff_borrow_detail.html')

# ประวัติการยืม
@login_required
def staff_borrowing_history_detail(req):
    return render(req,'pages/staff_borrowing_history_detail.html')

# ข้อมูลการคืนพัสดุ-ครุภัณฑ์
@login_required
def staff_borrowing_history(req):
    return render(req,'pages/staff_borrowing_history.html')

# จัดการรายการยืม
@login_required
def staff_index_borrow(req):
    return render(req,'pages/staff_index_borrow.html')

# จัดการรายการยืม
@login_required
def staff_index_borrownow(req):
    return render(req,'pages/staff_index_borrownow.html')

# จัดการรายการคืน
@login_required
def staff_index_return(req):
    return render(req,'pages/staff_index_return.html')

# จัดการข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
@login_required
def staff_introduction_detail(req):
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page
    }
    return render( req, 'pages/staff_introduction_detail.html', context)

# ข้อมูลการแนะนำพัสดุเข้าสู่ระบบ
@login_required
def staff_introduction_hisdetail(req):
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page
    }
    return render( req, 'pages/staff_introduction_hisdetail.html', context)

# รายละเอียดจัดการพัสดุ-ครุภัณฑ์
@login_required
def staff_manage_detail(req):
    return render(req,'pages/staff_manage_detail.html')

# จัดการพัสดุ
@login_required
def staff_manage_parcel(req):
    form = ParcelForm()

    if req.method == 'POST':
        form = ParcelForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staff_manage_parcel/')
    else:
        form = ParcelForm()
    AllParcel = Add_Parcel.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllParcel, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)        
    context = {
        "page" : page,
        "form" : form
    }
    return render(req, 'pages/staff_manage_parcel.html', context)  

@login_required
def delete_staff_manage_parcel(req, id):
    obj = Add_Parcel.objects.get(id=id)
    obj.delete()
    return redirect('staff_manage_parcel')

# จัดการครุภัณฑ์
@login_required
def staff_manage_durable(req):
    form = DurableForm()

    if req.method == 'POST':
        form = DurableForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staff_manage_durable/')
    else:
        form = DurableForm()
    AllDurable = Add_Durable.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllDurable, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)   

    context = {
        "page" : page,
        "form":form
    }

    return render(req, 'pages/staff_manage_durable.html', context)  

@login_required
def delete_staff_manage_durable(req, id):
    obj = Add_Durable.objects.get(id=id)
    obj.delete()
    return redirect('staff_manage_durable') 

# แก่ไขข้อมูลส่วนตัว และจัดการข้อมูลส่วนตัว
@login_required
def staff_personal_info(req):
    return render(req, 'pages/staff_personal_info.html')  

@login_required
def staff_personal_info_edit(req):
    return render(req, 'pages/staff_personal_info_edit.html')

@login_required
def staff_personal_info_edit(req):
    return render(req,'pages/staff_personal_info_edit.html')

@login_required
def staff_personal_info(req):
    return render(req,'pages/staff_personal_info.html')

# รายละเอียดรายงานการยืมพัสดุ
@login_required
def staff_report_borrowReport(req):
    return render(req,'pages/staff_report_borrowReport.html')

# รายงานจำนวนรายการพัสดุที่จำหน่ายทิ้ง
@login_required
def staff_report_dispose(req):
    return render(req,'pages/staff_report_dispose.html')

# รายงานภาพรวมพัสดุ
def staff_report(req):
    AllRecList = ListFromRec.objects.all()
    AllRecList_count = AllRecList.count()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page,
        "AllRecList_count" : AllRecList_count
    }
    return render( req, 'pages/staff_report.html', context)


# รายงานจำนวนรายการพัสดุที่คงเหลือในระบบ
@login_required
def staff_report_remaining(req):
    return render(req,'pages/staff_report_remaining.html')

# รายงานการยืมทั้งหมด
@login_required
def staff_Including_borrowing(req):
    return render(req,'pages/staff_Including_borrowing.html')
