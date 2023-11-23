from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

import user_profiles
from kavete.models import BlogPost, Tag
from user_profiles.models import UserProfile


def home(request):
    all_posts = BlogPost.objects.all().order_by('-date_published')
    paginator = Paginator(all_posts, per_page=2)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'home.html', {'all_posts': data})


def full_blog_post(request, post_id):
    blog_post = BlogPost.objects.get(pk=post_id)
    tags = blog_post.tags.all()
    random_posts = BlogPost.objects.order_by('?')[:5]
    post_tags = blog_post.tags.all()
    related_posts = BlogPost.objects.filter(tags__in=post_tags).exclude(pk=post_id).distinct()[:5]
    all_tags = Tag.objects.all()
    context = {
        'blog_post': blog_post,
        'tags': tags,
        'random_posts': random_posts,
        'related_posts': related_posts,
        'all_tags': all_tags,
    }
    return render(request, 'blog.html', context)


def search_posts(request):
    search_word = request.GET["search_word"]
    all_posts = BlogPost.objects.filter(Q(title__icontains=search_word) | Q(category__icontains=search_word) |
                                        Q(author__first_name__icontains=search_word) |
                                        Q(author__last_name__icontains=search_word))
    paginator = Paginator(all_posts, per_page=10)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    # TODO Use Elastic search instead
    return render(request, 'home.html', {'all_posts': data})


def get_random_posts(request, post_id):
    random_posts = BlogPost.objects.all().order_by('?')[:10]
    return {
        'random_posts': random_posts
    }


def get_posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts_with_tag = BlogPost.objects.filter(tags=tag)
    paginator = Paginator(posts_with_tag, per_page=2)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    context = {
        'tag': tag,
        'post_with_tag': data
    }
    return render(request, 'posts_by_tag.html', context)
