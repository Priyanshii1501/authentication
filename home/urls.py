from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path('', views.index , name="home"),
    path("login" , views.loginUser , name="login"),
    path("logout" , views.logoutUser , name="logout"),
    path("add_user" , views.add_user , name="add_user"),
    path("delete_user/<int:user_id>" , views.delete_user , name="delete_user"),
    path("update_user/<int:user_id>" , views.update_user , name="update_user"),
    path("do_update_user/<int:user_id>" , views.do_update_user , name="do_update_user"),
]
