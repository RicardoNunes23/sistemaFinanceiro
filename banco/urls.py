from django.contrib import admin
from django.urls import path
from django.conf import settings


from . import views

 
urlpatterns = [
    

    path('banco/', views.banco, name='banco'),
    path('bancoView/<int:id>', views.bancoView, name='bancoView'),
    path('bancoAdd/', views.bancoAdd, name='bancoAdd'),
    path('bancoEdit/<int:id>', views.bancoEdit, name='bancoEdit'),
   
]
