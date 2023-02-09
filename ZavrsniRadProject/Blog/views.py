from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates/Blog/index.html')

def singlePost(request):
    return render(request, 'templates/Blog/singlePost.html')