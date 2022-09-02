from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.db.models import Q


def all_blogs(request):
    search_query = request.GET.get('search', '')
    if search_query:
        blogs = Blog.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    else:
        blogs = Blog.objects.all()

    paginator = Paginator(blogs, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'blog/all_blogs.html', context)


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
