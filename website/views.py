from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_view(request):
    return render(request, "website/index.html")


def about_view(requst):
    return render(requst, "website/about.html")


def contact_view(requst):
    return render(requst, "website/contact.html")


def test_view(requst):
    context={'title': 'salam', 'content': '://'}
    return render(requst, "website/test.html",context)
