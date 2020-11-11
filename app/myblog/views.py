from django.shortcuts import render,HttpResponse,redirect
from .models import post,category,author,BlogComment
from django.contrib import messages
from myblog.templatetags import extras

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
        comments= BlogComment.objects.filter(post=posts, parent=None)
        replies= BlogComment.objects.filter(post=posts).exclude(parent=None)
        replyDict={}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno]=[reply]
            else:
                replyDict[reply.parent.sno].append(reply)
        context= {
            'post':posts,
            'comments':comments,
            'user':request.user,
            'replyDict':replyDict,
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
def blogComment(request):
    if request.method == 'POST':
        comment=request.POST.get('comment')
        user= request.user
        serial=request.POST.get('serial')
        posts= post.objects.get(srl=serial)
        parentSno= request.POST.get('parentSno')
        if parentSno=='':
            comment= BlogComment(comment=comment,user=user,post=posts)
            comment.save()
            messages.success(request,"Comment posted successfully")
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment= BlogComment(comment=comment,user=user,post=posts,parent=parent)
            comment.save()
            messages.success(request,"Reply posted successfully")
        return redirect(f'/blog/{posts.slug}')
    else:
        return HttpResponse('404 not found')