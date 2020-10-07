from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiview,name="apiview"),
    path('userlist',views.userlist,name="userlist"),
    path('userdetail/<str:pk>/',views.userdetail,name="userdetail"),
    path('usercreate/',views.usercreate,name="usercreate"),
    path('userupdate/<str:pk>/',views.userupdate,name="userupdate"),
    path('userdelete/<str:pk>/',views.userdelete,name="userdelete"),
]