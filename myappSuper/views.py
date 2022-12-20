from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from myappSuper.forms import *
from django.contrib.auth.decorators import login_required

@login_required
def admin_detail(req):
    return render(req, "pages/admin_detail.html")

@login_required
def admin_staff(req):
    return render(req, "pages/admin_staff.html")

@login_required
def admin_user(req):
    return render(req, "pages/admin_user.html")

@login_required
def admin_notifications(req):
    return render(req, "pages/admin_notifications.html")