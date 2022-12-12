from django.urls import path
from myappstaff import views
from .views import * 

urlpatterns = [
    # staff
    path('staff_borrow_detail/', staff_borrow_detail),
    path('staff_borrowing_history_detail/', staff_borrowing_history_detail),
    path('staff_borrowing_history/', staff_borrowing_history),
    path('staff_index_borrow/', staff_index_borrow),
    path('staff_index_borrownow/', staff_index_borrownow),
    path('staff_index_return/', staff_index_return),
    path('staff_introduction_detail', staff_introduction_detail),
    path('staff_introduction_hisdetail/', staff_introduction_hisdetail),
    path('staff_introduction/', staff_introduction),
    path('staff_introduction_history/', staff_introduction_history),
    
    path('staff_personal_info_edit/', staff_personal_info_edit),
    path('staff_personal_info/', staff_personal_info),
    
    path('staff_report_borrowReport/', staff_report_borrowReport),
    path('staff_report_dispose/', staff_report_dispose),
    path('staff_report_remaining/', staff_report_remaining),
    path('staff_Including_borrowing/', staff_Including_borrowing),
    
    path('staff_report/', views.staff_report, name="staff_report"),
   
    
    #path staff_setting
    path('staff_setting',views.staff_setting, name="staff_setting"), 
    path('deleteCategoryType/<int:id>',views.deleteCategoryType, name="deleteCategoryType"),
    path('edit_staff_setting/<int:id>',views.edit_staff_setting, name="edit_staff_setting"),
    
    #path manage parcel durable
    path('staff_manage_detail/', staff_manage_detail),
    path('staff_manage_parcel/', views.staff_manage_parcel, name="staff_manage_parcel"), #add parcel
    path('delete_staff_manage_parcel/<int:id>',views.delete_staff_manage_parcel, name="delete_staff_manage_parcel"),
    
    path('staff_manage_durable/', views.staff_manage_durable, name="staff_manage_durable"),#add durable
    
    path('staff_setting_status',views.staff_setting_status, name='staff_setting_status'),
    path('DeleteCategoryStatus/<int:id>',views.DeleteCategoryStatus, name="DeleteCategoryStatus"),
    path('edit_staff_setting_status/<int:id>',views.edit_staff_setting_status, name="edit_staff_setting_status"),
    
]
