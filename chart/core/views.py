from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'examp.html', context)

def bar(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'bar.html', context)

def radar(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'radar.html', context)

def line(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'line.html', context)

def pie(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'pie.html', context)

def scutter(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'scutter.html', context)

def donut(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'donut.html', context)
