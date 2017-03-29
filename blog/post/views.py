from django.shortcuts import render
from post.models import Category
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class CategoryView(ListView):
    model = Category
    template_name = 'category_list.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, self.template_name, {'category_list': categories})


class PostView(ListView):
    pass


