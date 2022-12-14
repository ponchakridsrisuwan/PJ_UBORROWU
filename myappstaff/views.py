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

def deleteCategoryType(req, id):
    obj = CategoryType.objects.get(id=id)
    obj.delete()
    return redirect('/staff_setting')

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

def DeleteCategoryStatus(req, id):
    obj = CategoryStatus.objects.get(id=id)
    obj.delete()
    return redirect('/staff_setting_status')

def edit_staff_setting_status(req,id):
    obj = CategoryStatus.objects.get(id=id)
    obj.name_CategoryStatus = req.POST['name_CategoryStatus']
    obj.save()
    return redirect('/staff_setting_status')

# การแนะนำพัสดุเข้าสู่ระบบ    
@login_required
def staff_introduction(req):
    AllRecList = ListFromRec.objects.all()
    page_num = req.GET.get('page', 1)
    p = Paginator(AllRecList, 10)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)            
    context = {
        'page' :page,
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
def staff_manage_parcel(request):
    form = ParcelForm()

    if request.method == 'POST':
        form = ParcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staff_manage_parcel/')
    else:
        form = ParcelForm()

    context = {
        "form":form
    }

    return render(request, 'pages/staff_manage_parcel.html', context)  


# def staff_manage_parcel(req):
#     if req.method == "POST":
#         username = req.user
#         name = req.POST.get('name')
#         name_CategoryType = CategoryType.objects.get(id = req.POST.get('name_CategoryType'))
#         quantity = req.POST.get('quantity')
#         numdate = req.POST.get('numdate')
#         description = req.POST.get('description')
#         image = req.POST.get('image')
#         date = timezone.now()
#         obj = Add_Parcel(username=username, name=name, name_CategoryType=name_CategoryType, quantity=quantity, 
#                           numdate=numdate, image=image, description=description, date=date)
#         obj.save()
#         return redirect('/staff_manage_parcel/')   
#     else:
#         obj = Add_Parcel()   
#     obj = Add_Parcel.objects.all()   
#     AllParcel = Add_Parcel.objects.all()
#     page_num = req.GET.get('page', 1)
#     p = Paginator(AllParcel, 10)
#     try:
#         page = p.page(page_num)
#     except:
#         page = p.page(1)        
#     context = {
#         "AllParcel": Add_Parcel.objects.all(),
#         "All_CategoryType": CategoryType.objects.all(),
#         "page" : page,
#     }
#     print(Add_Parcel.objects.all())
#     return render(req, 'pages/staff_manage_parcel.html', context)  

# จัดการครุภัณฑ์
@login_required
def staff_manage_durable(request):
    form = DurableForm()

    if request.method == 'POST':
        form = DurableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/staff_manage_durable/')
    else:
        form = DurableForm()
    # form = DurableForm.objects.all()   
    DurableAll = DurableForm.objects.all()
    # page_num = request.GET.get('page', 1)
    # p = Paginator(DurableAll, 10)
    # try:
    #     page = p.page(page_num)
    # except:
    #     page = p.page(1) 

    context = {
        "form":form,
        "DurableAll":DurableAll.objects.all(),
        # "page" : page,
    }

    return render(request, 'pages/staff_manage_durable.html', context)  


# def staff_manage_durable(req):
#     if req.method == "POST":
#         username = req.user
#         name = req.POST.get('name')
#         name_CategoryType = CategoryType.objects.get(id = req.POST.get('name_CategoryType'))
#         #name_CategoryType = CategoryType(queryset=CategoryType.objects.all(), required=False)
#         quantity = req.POST.get('quantity')
#         numdate = req.POST.get('numdate')
#         description = req.POST.get('description')
#         image = req.POST.get('image')
#         date = timezone.now()
#         obj = Add_Durable(username=username, name=name, name_CategoryType=name_CategoryType, quantity=quantity, 
#                           numdate=numdate, image=image, description=description, date=date)
#         obj.save()
#         return redirect('/staff_manage_durable')   
#     else:
#         obj = Add_Durable()   
#     obj = Add_Durable.objects.all()   
#     AllDurable = Add_Durable.objects.all()
#     page_num = req.GET.get('page', 1)
#     p = Paginator(AllDurable, 10)
#     try:
#         page = p.page(page_num)
#     except:
#         page = p.page(1)        
#     context = {
#         "AllDurable": Add_Durable.objects.all(),
#         "page" : page,
#     }
#     return render(req, 'pages/staff_manage_durable.html', context)  

# แก่ไขข้อมูลส่วนตัว และจัดการข้อมูลส่วนตัว
@login_required
def staff_personal_info(req):
    return render(req, 'pages/staff_personal_info.html')  

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
@login_required
def staff_report(req):
    return render(req,'pages/staff_report.html')

# รายงานจำนวนรายการพัสดุที่คงเหลือในระบบ
@login_required
def staff_report_remaining(req):
    return render(req,'pages/staff_report_remaining.html')

# รายงานการยืมทั้งหมด
@login_required
def staff_Including_borrowing(req):
    return render(req,'pages/staff_Including_borrowing.html')
