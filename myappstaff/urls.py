from django.urls import path
from myappstaff import views
from .views import * 

urlpatterns = [
    # staff
    path('staff_borrow_detail/', views.staff_borrow_detail, name="staff_borrow_detail"),
    path('staff_borrowing_history_detail', views.staff_borrowing_history_detail, name="staff_borrowing_history_detail"),
    path('staff_borrowing_history/', views.staff_borrowing_history, name="staff_borrowing_history"),
    path('staff_index_borrow', views.staff_index_borrow, name="staff_index_borrow"),
    path('staff_index_borrownow', views.staff_index_borrownow, name="staff_index_borrownow"),
    path('staff_index_return', views.staff_index_return, name="staff_index_return"),
    
    path('staff_introduction_detail/<int:id>', views.staff_introduction_detail, name="staff_introduction_detail"),
    path('staff_introduction', views.staff_introduction, name="staff_introduction"),
    path('staff_introduction_update/<int:id>', views.staff_introduction_update, name="staff_introduction_update"),
    path('staff_introduction_history', views.staff_introduction_history, name="staff_introduction_history"),
    
    path('staff_personal_info_edit/', views.staff_personal_info_edit, name="staff_personal_info_edit"),
    path('staff_personal_info/', views.staff_personal_info, name="staff_personal_info"),
    
    path('staff_report_borrowReport/', views.staff_report_borrowReport, name="staff_report_borrowReport"),
    path('staff_report_dispose', views.staff_report_dispose, name="staff_report_dispose"),
    path('staff_report_remaining/', views.staff_report_remaining, name="staff_report_remaining"),
    path('staff_Including_borrowing/', views.staff_Including_borrowing, name="staff_Including_borrowing"),
    
    path('staff_notifications/',views.staff_notifications, name="staff_notifications"),
    
    path('staff_report/', views.staff_report, name="staff_report"),
    
    #path staff_setting
    path('staff_setting',views.staff_setting, name="staff_setting"), 
    path('deleteCategoryType/<int:id>',views.deleteCategoryType, name="deleteCategoryType"),
    path('edit_staff_setting/<int:id>',views.edit_staff_setting, name="edit_staff_setting"),
    
    #path manage parcel durable
    path('staff_manage_detail/', views.staff_manage_detail),
    path('staff_manage_parcel/', views.staff_manage_parcel, name="staff_manage_parcel"), #add parcel
    path('delete_staff_manage_parcel/<int:id>',views.delete_staff_manage_parcel, name="delete_staff_manage_parcel"),
    
    path('staff_manage_durable/', views.staff_manage_durable, name="staff_manage_durable"),#add durable
    path('delete_staff_manage_durable/<int:id>',views.delete_staff_manage_durable, name="delete_staff_manage_durable"),

    path('staff_setting_status',views.staff_setting_status, name='staff_setting_status'),
    path('DeleteCategoryStatus/<int:id>',views.DeleteCategoryStatus, name="DeleteCategoryStatus"),
    path('edit_staff_setting_status/<int:id>',views.edit_staff_setting_status, name="edit_staff_setting_status"),
    
]
