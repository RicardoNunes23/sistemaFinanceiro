from django.urls import path

from . import views

 
urlpatterns = [
     
    path('subconta/', views.subconta, name='subconta'),
    path('subcontaAdd/',views.subcontaAdd, name='subcontaAdd'),
    path('subcontaEdit/<int:id>',views.subcontaEdit, name='subcontaEdit'),
    path('subcontaDel/<int:id>',views.subcontaDel, name='subcontaDel'),


]