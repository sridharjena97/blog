from django.shortcuts import render,HttpResponse
from .models import post

# Create your views here.
def blogHome(request):
    posts= post.objects.all()
    print(posts)
    context= {
        'endp': 'blog',
        'posts':posts
        }
    return render(request,'myblog/blogHome.html', context)
def blogPost(request,slug):
    return HttpResponse(f'this is blog for {slug}')