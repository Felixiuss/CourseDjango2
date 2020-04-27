from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post, Comment, Tag


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
        # tags = post.get_tags()  # вызов метода модели Post, но удобней вызывать прямо из шаблона (это просто пример)
        # print(tags)
        return render(request, post.template, {'categories': category_list, 'post': post})


class CategoryView(View):
    """Output of category articles"""
    # posts = []
    def get(self, request, category_slug=None, slug=None):
        if category_slug:
            posts = Post.objects.filter(
                category__slug=category_slug, category__published=True, published=True
            )
        else:
            posts = Post.objects.filter(tags__slug=slug, published=True)
        if posts:  # if posts.exists()
            template = posts.first().get_category_template()  # тоже что posts[0].get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'post_list': posts})


# class TagView(View):
#     """Output articles by tag"""
#     def get(self, request, slug):
#         posts = Post.objects.filter(tags__slug=slug, published=True)
#         return render(request, posts.first().get_category_template(), {'post_list': posts})
