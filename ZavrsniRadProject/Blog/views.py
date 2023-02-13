from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    postList = Post.objects.all().order_by('-id')
    context = {
        'postData':postList,
    }
    
    return render(request, 'Blog/index.html', context=context)

def singlePost(request, postID):
    postList = Post.objects.get(pk=postID)
    context = {
        'postData':postList,
    }
    
    return render(request, 'Blog/singlePost.html', context=context)