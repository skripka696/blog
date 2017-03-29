from django.http.response import HttpResponse
from django.shortcuts import render
from post.models import Category, Post
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CategoryView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {'nodes': categories})


class CategoryDetailView(ListView):
    model = Post
    template_name = 'category_detail_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(category__id=kwargs['pk'])
        return render(request, self.template_name, {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostView(ListView):
    pass


