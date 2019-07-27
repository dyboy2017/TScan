from django.urls import path
from . import views

# 配置URL
urlpatterns = [
    path('infoleak', views.infoleak, name='infoleak'),
    path('webside', views.webside, name='webside'),
    path('portscan', views.portscan, name='portscan'),
    path('', views.index, name='index'),
]

