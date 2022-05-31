from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    POSTS_ON_VIEW: int = 10
    template = 'posts/index.html'
    posts = Post.objects.all()[:POSTS_ON_VIEW]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    POSTS_ON_VIEW: int = 10
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    posts = group.posts.order.by('-pub_date')[:POSTS_ON_VIEW]
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
