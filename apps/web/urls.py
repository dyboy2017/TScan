from django.urls import path
from . import views

# 配置URL
urlpatterns = [
    path(r'portscan', views.portscan, name='portscan'),
    path('', views.index, name='index'),

]

