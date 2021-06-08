from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('addpet', views.addpet),
    path('user/<int:userid>', views.user),
    path('user/<int:userid>/makeapp', views.makeappointment),
]
