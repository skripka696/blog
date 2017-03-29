from django.conf.urls import url
from django.contrib import admin
from post import views

urlpatterns = [
    url(r'^categories/$', views.CategoryView.as_view(), name='category_list'),
]
