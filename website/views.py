from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_view(requst):
    return render(requst,"website/index.html")
def about_view(requst):
    return render(requst,"website/about.html")
def contact_view(requst):
    return render(requst,"website/contact.html")
