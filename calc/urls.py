from os import name
from django.urls import path


from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('signup',views.signup, name="signup"),
    path('blood_rgistration',views.blood_rgistration,name='blood_rgistration'),
    path('add',views.add, name='add'),
    path('register',views.register, name='register'),
    path('display',views.display,name='display'),
    path('logout',views.logout,name='logout')
]