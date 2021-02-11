from django.urls import path

from . import views

 
urlpatterns = [
          
    path('conta/', views.conta, name='conta'),
    path('contaAdd/',views.contaAdd, name='contaAdd'), 

    

]