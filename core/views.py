from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
     return render(request, 'core/index.html')

def about(request):
     return render(request, 'core/pages/about.html')


def store(request):
     return render(request, 'core/pages/store.html')

