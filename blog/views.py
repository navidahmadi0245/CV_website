from django.shortcuts import render


# Create your views here.
def blog_view(requst):
    return render(requst, "blog/blog.html")


def single_view(requst):
    return render(requst, "blog/single-blog.html")
