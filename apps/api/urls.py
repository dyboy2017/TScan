from django.urls import path
from . import views


# 配置URL
urlpatterns = [
    path('portscan', views.port_scan, name='portscan'),
    path('whatcms', views.what_cms, name='whatcms'),
    path('iswaf', views.is_waf, name='iswaf'),
    path('isexistcdn', views.isexistcdn, name='cdncheck'),
    path('webweight', views.webweight, name='webweight'),
    path('baseinfo', views.baseinfo, name='baseinfo'),
    path('', views.index, name='index'),
]

