from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'Blog/index.html')

def singlePost(request, postID):
    postList = Post.objects.get(pk=postID)
    context = {
        'postData':postList,
    }
    print(context)
    return render(request, 'Blog/singlePost.html', context=context)