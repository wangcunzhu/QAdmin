from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.do_login, name='do_login'),
    path('^do_login/$', views.do_login, name='do_login'),
]
