from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html',{'endp':'home'})
def contact(request):
    return render(request, 'home/contact.html', {'endp':'contact'})
def about(request):
    return render(request, 'home/about.html', {'endp':'about'})