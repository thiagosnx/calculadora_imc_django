

from django.urls import path
from app_calculadora import views

urlpatterns = [
    # rota,view,nome de ref
    #projeto2.com
    path('',views.home,name='home'),
    #projeto2.com/calculo
    path('/calcular', views.calcular,name='calcular')


]


