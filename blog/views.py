from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
# Create your views here.

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    try:
        post = get_object_or_404(Post, slug=post, status=Post.Status.PUBLISHED, publish__year=year, publish__month=month, publish__day=day)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/post/detail.html', {'post': post})
