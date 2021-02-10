from django.urls import path
from . import views

urlpatterns = [
  

    path('centroDeCusto/', views.centroDeCusto, name='centroDeCusto'),
    path('centroDeCustoAdd/', views.centroDeCustoAdd, name='centroDeCustoAdd'),

   
 
]