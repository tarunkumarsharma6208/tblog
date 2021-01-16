from django.shortcuts import render, get_object_or_404
from .models import *


def home(request, category_slug=None):
    category_page = None
    post_list = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        post_list = Post.objects.filter(category=category_page)
    else:
        post_list = Post.objects.all().filter()

    return render(request, 'blog/home.html', {'category': category_page, 'post_list': post_list})


def article_detail(request, category_slug, post_slug):
    try:
        post_detail = Post.objects.get(category__slug=category_slug, slug=post_slug)
    except Exception as e:
        raise e
    return render(request, 'blog/detail_view.html', {'post_detail': post_detail})


def login(request):
    return render(request, 'blog/login.html')


def register(request):
    return render(request, 'blog/register.html')


def about(request):
    return render(request, 'blog/about.html')