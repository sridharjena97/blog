from django.shortcuts import render,HttpResponse,redirect
from .models import post,category,author,BlogComment
from django.contrib import messages
from myblog.templatetags import extras

# Create your views here.
# Blog Post View page
def blogPost(request,slug):
    try:
        posts= post.objects.get(slug=slug)
        posts.clickRate= posts.clickRate + 1
        posts.save()
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
# All category view page
def allCat(request):
    cats= category.objects.all()
    context= {
        'cats':cats
        }
    return render(request,'myblog/allcat.html',context)
    # return HttpResponse('this is all cat page')
# Views of post within a category
def catView(request,cat):
    posts= post.objects.filter(category=cat)
    cat= category.objects.get(srl=cat)
    context= {
        'posts':posts,
        'cat':cat
        }
    return render(request,'myblog/catview.html',context)
# View of authors of this website
def authView(request,auth):
    auth= author.objects.get(name=auth)
    context= {
        'auth':auth
        }
    return render(request,'myblog/authorpage.html',context)
# API for handelling comments of blog
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