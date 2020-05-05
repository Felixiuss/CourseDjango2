from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Category, Post, Comment, Tag
from .forms import CommentForm


class PostListView(View):
    """Output of category articles"""
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, slug=None):
        # category_list = Category.objects.filter(published=True)
        if category_slug:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif slug:
            posts = self.get_queryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_queryset()
        if posts:  # if posts.exists()
            template = posts.first().get_category_template()  # тоже что posts[0].get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'post_list': posts})


class PostDetailView(View):
    """Showing a specific article"""
    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        form = CommentForm()
        return render(
            request, post.template, {'categories': category_list, 'post': post, 'form': form}
        )

    def post(self, request, **kwargs):
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get("slug"))
            form.author = request.user
            form.save()
        return redirect(request.path)

