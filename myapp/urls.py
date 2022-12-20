from django.urls import path
from .views import * 
from myapp import views

urlpatterns = [
    path('',HomePage, name="user_index"),
    path('register/',user_register, name="register"), 
    path('user_borrow/',user_borrow, name="user_borrow"), 
    path('user_borrowed/',user_borrowed, name="user_borrowed"), 
    path('user_history/',user_history, name="user_history"), 
    path('user_cart/',user_cart, name="user_cart"), 
    path('user_detail/',user_detail, name="user_detail"), 
    path('user_durable_articles/',user_durable_articles, name="user_durable_articles"), 
    path('user_notifications/',user_notifications, name="user_notifications"), 
    
    path('user_recommend',views.user_recommend, name="user_recommend"), 
    path('user_recommend_edit/<int:id>',views.user_recommend_edit, name="user_recommend_edit"),
    path('deleteRecList/<int:id>', views.deleteRecList, name="deleteRecList"),
    path('user_recommend_history/',views.user_recommend_history, name="user_recommend_history"), 
    path('user_recommend_detail/<int:id>', views.user_recommend_detail, name="user_recommend_detail"),
    
    path('user_personal_info/',views.user_personal_info, name="user_personal_info"), 
    
    
]