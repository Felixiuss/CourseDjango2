from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post


# def home(request):
#     if request.method == "POST":
#         return HttpResponse('Hi')
#     else:
#         return HttpResponse('Good')


class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})


class PostDetailView(View):
    """Showing a specific article"""
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {'categories': category_list, 'post': post})


class CategoryView(View):
    """Output of category articles"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})

