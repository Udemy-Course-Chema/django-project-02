from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
     return render(request, 'core/index.html')

def about(request):
     return render(request, 'core/pages/about.html')

def services(request):
     return render(request, 'core/pages/services.html')

def store(request):
     return render(request, 'core/pages/store.html')

def contact(request):
     return render(request, 'core/pages/contact.html')

def blog(request):
     return render(request, 'core/pages/blog.html')