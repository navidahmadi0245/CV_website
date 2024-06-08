from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime


# Create your views here.
def blog_view(requst):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')
    context = {"posts": posts}
    return render(requst, "blog/blog.html", context)


def single_view(requst, pid):
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=datetime.now())
    context = {"post": post}
    post.counted_view += 1
    post.save()
    return render(requst, "blog/single-blog.html", context)
