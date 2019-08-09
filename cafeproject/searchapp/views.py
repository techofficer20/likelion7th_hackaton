from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', 
    {
        'post' : post
    })

def result(request):
    post = Post.objects.all()
    obj_title = request.GET['title']
    obj_location = request.GET['location']
    obj_feature = request.GET['feature']
    return render(request, 'result.html', 
    {
        'post' : post,
        'obj_title' : obj_title,
        'obj_location' : obj_location,
        'obj_feature' : obj_feature
    })