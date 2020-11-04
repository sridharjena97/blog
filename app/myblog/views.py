from django.shortcuts import render,HttpResponse
from .models import post,category,author

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
    try:
        posts= post.objects.get(slug=slug)
        context= {
            'post':posts,
            'found':True
            }   
    except: 
        context= {
            'found':False
            } 
    return render(request,'myblog/blogView.html',context)
def allCat(request):
    cats= category.objects.all()
    context= {
        'cats':cats
        }
    return render(request,'myblog/allcat.html',context)
    # return HttpResponse('this is all cat page')
def catView(request,cat):
    posts= post.objects.filter(category=cat)
    cat= category.objects.get(srl=cat)
    print(cat)
    context= {
        'posts':posts,
        'cat':cat
        }
    return render(request,'myblog/catview.html',context)
def authView(request,auth):
    auth= author.objects.get(name=auth)
    context= {
        'auth':auth
        }
    return render(request,'myblog/authorpage.html',context)