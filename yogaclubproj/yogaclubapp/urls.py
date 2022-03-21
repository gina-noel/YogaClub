from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('pricing/', views.pricing, name='pricing'),
    path('classes/', views.classes, name='classes'),
    path('classdetail/<int:id>', views.classdetail, name='classdetail'),  
    path('newclass/', views.newClass, name='newclass'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]