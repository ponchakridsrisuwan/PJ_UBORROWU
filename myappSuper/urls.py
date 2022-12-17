from django.urls import path
from myappSuper.views import *
from . import views

urlpatterns = [
    path('admin_detail/',admin_detail),
    
    path('admin_user_setting/',views.admin_user_setting, name="admin_user_setting"),
    path('admin_staff_setting/',views.admin_staff_setting, name="admin_staff_setting"),
    
    path('admin_user/',views.admin_user),
    path('admin_staff/',views.admin_staff),
    
    path('SearchStaff/',views.SearchStaff),
    path('SearchUser/',views.SearchUser),

    path('deleteUser/<int:id>',views.deleteUser, name="deleteUser"),
    path('deleteStaff/<int:id>', views.deleteStaff, name="deleteStaff"),
]