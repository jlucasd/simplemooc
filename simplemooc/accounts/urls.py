from django.conf.urls import url
from django.contrib.auth import views as viewsauth

urlpatterns = [
    url(r'^entrar/$', viewsauth.login, {'template_name': 'accounts/login.html' }, name='login'),
]
