from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.home, name='home'),
    path('form-clientes/', views.form_clientes, name='form-clientes'),
]
