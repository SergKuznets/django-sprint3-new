from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category

LAST_POST = 5


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    template_name = 'blog/index.html'
    posts = get_published_posts()[:LAST_POST]
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def post_detail(request, pk):
    post = get_object_or_404(
        get_published_posts(),
        pk=pk,
    )
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = get_published_posts().filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)
