from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'post' : post})

def result(request):
    post = Post.objects.all()
    obj = request.GET['searching'] # 검색어 데이터 얻어냄
    obj_list = obj.split(' ')
    return render(request, 'result.html', {'post' : post, 'obj' : obj, 'obj_list' : obj_list}) # 검색어 데이터를 html에 표현하기 위해 딕셔너리 추가