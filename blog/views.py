from django.shortcuts import render
from .models import Category, Post

# Create your views here.
def blog(request):
     
     return render(request, 'blog/blog.html')