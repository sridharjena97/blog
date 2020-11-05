from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from myblog.models import post,category
from django.contrib import messages
from django.contrib.auth.models import User
import re

# Create your views here.
def home(request):
    posts= post.objects.all()[:3]
    cats= category.objects.all()
    context= {
        'endp': 'home',
        'posts':posts,
        'categories': cats
        }
    return render(request, 'home/index.html',context)
def contact(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        mobile= request.POST.get('mobile','')
        title= request.POST.get('title','')
        message= request.POST.get('message','')
        newQuery= Contact(name=name, email=email, mobileNumber=mobile, messageTitle=title, messageBody=message)
        newQuery.save()
        messages.success(request, "Submitted Successfully")
    return render(request, 'home/contact.html', {'endp':'contact'})
def about(request):
    return render(request, 'home/about.html', {'endp':'about'})
def search(request):
    query=request.GET['query']
    if len(query)>50:
        posts= post.objects.none()
        print('no post')
    else:
        postTitle= post.objects.filter(title__icontains=query)
        postDesc= post.objects.filter(desc__icontains=query)
        posts= postTitle.union(postDesc)
    print(posts.count())
    if posts.count()== 0:
        context= {
            'query':query,
            }
    else:
        context= {
            'posts':posts,
            'resultFound':True,
            'query':query,
            }
    return render(request, 'home/search.html', context)
def handleSignup(request):
    if request.method== 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        sEmail= request.POST['sEmail']
        sUserName= request.POST['sUserName']
        sPassword= request.POST['sPassword']
        cPassword= request.POST['cPassword']
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        # checks for data received
        if User.objects.filter(username=sUserName).count()>0:
            messages.error(request,"user name already taken. Try with diiferent username")
            return redirect('home')
        if User.objects.filter(email=sEmail).count()>0:
            messages.error(request,"Email already registered. Try to login or Use a different email address")
            return redirect('home')
        if len(fname)<3 or len(lname)<3 or len(sEmail)<10 or len(sUserName)<8 or len(sPassword)<8:
            messages.error(request,"Check length of chracters entered and try again.")
            return redirect('home')
        if sPassword != cPassword:
            messages.error(request,"Password Does not match. Please Try again.")
            return redirect('home')
        if (re.search(regex,sEmail)) == None:
            messages.error(request,"Enter a valid email")
            return redirect('home')
        if not sUserName.isalnum():
            messages.error(request,"Enter a valid username")
            return redirect('home')
            
        # creating user
        myUser= User.objects.create_user(username=sUserName,email=sEmail,password=sPassword,first_name=fname,last_name=lname)
        myUser.save()
        messages.success(request,"you are successfully signedup to our website.")
        return redirect('home')
    else:
        return HttpResponse('404- Not Found')