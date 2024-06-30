from django import template
from blog.models import Post, Category
from datetime import datetime

register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.filter
def snippet(text, args=50):
    return text[:args]


@register.inclusion_tag('blog/blog-latest-post.html')
def latest_posts(args=2):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('published_date')
    return {'posts': posts}
