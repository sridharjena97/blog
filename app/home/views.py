from django.shortcuts import render,HttpResponse
from home.models import Contact
from myblog.models import post,category
from django.contrib import messages

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