from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category


# def home(request):
#     if request.method == "POST":
#         return HttpResponse('Hi')
#     else:
#         return HttpResponse('Good')


class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        # print(category_list)
        return render(request, 'blog/home.html', {'categories': category_list})


class CategoryView(View):
    """Output of category articles"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})

