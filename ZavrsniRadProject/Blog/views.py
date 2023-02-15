from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    postList = Post.objects.filter(published=True).order_by('-id')
    context = {
        'postData':postList,
    }
    
    return render(request, 'Blog/index.html', context=context)


def posts(request):
    postList = Post.objects.filter(published=True).order_by('-id')
    context = {
        'postData':postList,
    }   
    return(render(request, 'Blog/posts.html', context=context))


def singlePost(request, postID):
    postList = Post.objects.get(pk=postID)
    context = {
        'postData':postList,
    }
    
    return render(request, 'Blog/singlePost.html', context=context)


def about(request):
    context={}
    return(render(request, 'Blog/about.html', context=context))

def contact(request):
    context={}
    return(render(request, 'Blog/contact.html', context=context))
