from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/index.html',{'endp':'home'})
def contact(request):
    if request.method=='POST':
        name= request.POST.get('name','')
        email= request.POST.get('email','')
        mobile= request.POST.get('mobile','')
        title= request.POST.get('title','')
        message= request.POST.get('message','')
        newQuery= Contact(name=name, email=email, mobileNumber=mobile, messageTitle=title, messageBody=message)
        newQuery.save()
        return render(request, 'home/contact.html', {'endp':'contact','deliverd':True})
    return render(request, 'home/contact.html', {'endp':'contact'})
def about(request):
    return render(request, 'home/about.html', {'endp':'about'})