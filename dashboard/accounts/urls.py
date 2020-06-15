from django.urls import path
from . import views


urlpatterns = [
    path('', views.account),
    path('login/', views.login),
    path('register/', views.register),
    path('merchant_register/', views.merchant_register),
]