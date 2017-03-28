from django.conf.urls import url
from django.contrib import admin
from user_profile import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='home'),
    url(r'^registration/$', views.Registration.as_view(), name='registr'),
]
