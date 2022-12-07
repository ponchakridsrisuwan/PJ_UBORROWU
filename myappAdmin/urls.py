from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('admin_detail/',admin_detail),
    path('admin_login/',admin_login),
    
    path('admin_user_setting/',views.Add_user),
    path('admin_staff_setting/',views.Add_staff),
    
    path('admin_user/',views.All_user),
    path('admin_staff/',views.All_staff),
    
    path('SearchStaff',views.SearchStaff),
    path('SearchUser',views.SearchUser),
    
    path('DeleteStaff/<int:id>',views.DeleteStaff),
    path('DeleteUser/<int:id>',views.DeleteUser),
]
