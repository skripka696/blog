from django.conf.urls import url
from django.contrib import admin
from post import views

urlpatterns = [
    url(r'^categories/$', views.CategoryView.as_view(), name='category_list'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name='category_detail_list'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
]
