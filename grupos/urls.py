from django.urls import path

from . import views

app_name = 'grupos'

urlpatterns = [
    path('', views.home, name='home'),
]
