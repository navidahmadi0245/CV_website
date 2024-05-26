from django.shortcuts import render, get_object_or_404
from blog.models import Post


# Create your views here.
def blog_view(requst):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(requst, "blog/blog.html", context)


def single_view(requst, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {"post": post}
    return render(requst, "blog/single-blog.html", context)
