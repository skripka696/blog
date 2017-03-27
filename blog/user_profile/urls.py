from django.conf.urls import url
from django.contrib import admin
from user_profile import views

urlpatterns = [
    url(r'^$', views.Login.as_view()),
    url(r'^registration/$', views.Registration.as_view()),
]
