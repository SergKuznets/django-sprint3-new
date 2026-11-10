from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category
from .constants import COUNT_POST_MAIN


def filter_posts(queryset):
    return queryset.select_related(
        'author',
        'location',
        'category'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    posts = filter_posts(Post.objects.all())[:COUNT_POST_MAIN]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(
        filter_posts(Post.objects.all()),
        pk=pk,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = filter_posts(category.posts.all())
    return render(
        request, 'blog/category.html',
        {
            'category': category,
            'posts': posts
        }
    )
