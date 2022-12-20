from django.urls import path
from myappSuper.views import *
from . import views

urlpatterns = [
    path('admin_detail',admin_detail),
    path('admin_notifications/',views.admin_notifications, name="admin_notifications"),
    path('admin_user/',views.admin_user, name="admin_user"),
    path('admin_staff/',views.admin_staff, name="admin_staff"),
]