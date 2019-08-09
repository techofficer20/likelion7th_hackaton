from django.shortcuts import render, redirect
from .models import Post, Location, Feature, Star
# Create your views here.

def index(request):
    post = Post.objects.all()
    location_list = Location.objects.all()
    feature_list = Feature.objects.all()
    star_list = Star.objects.all()
    return render(request, 'index.html', 
    {
        'post' : post, 
        'location_list' : location_list,
        'feature_list' : feature_list,
        'star_list' : star_list
    })

def result(request):
    post = Post.objects.all()
    location_list = Location.objects.all()
    feature_list = Feature.objects.all()
    star_list = Star.objects.all()
    obj_location = request.GET['location'] # 검색어 데이터 얻어냄
    obj_feature = request.GET['feature']
    return render(request, 'result.html', 
    {
        'post' : post,
        'location_list' : location_list,
        'feature_list' : feature_list,
        'star_list' : star_list, 
        'obj_location' : obj_location,
        'obj_feature' : obj_feature
    })