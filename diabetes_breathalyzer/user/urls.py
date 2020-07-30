from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='plogin'),
    path('dashboard/',views.dashboard, name= 'pdashboard'),
    path('logout/',views.logout,name='plogout'),
    path('profile/',views.profile , name='pprofile'),
    path('change_pass/',views.change_pass , name='ppasschange'),
    path('records/',views.prev_readings , name='pprevreadings'),
]