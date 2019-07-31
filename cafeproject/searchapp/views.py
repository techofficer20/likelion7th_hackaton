from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def result(request):
    obj = request.GET['searching'] # 검색어 데이터 얻어냄
    return render(request, 'result.html', {'obj' : obj}) # 검색어 데이터를 html에 표현하기 위해 딕셔너리 추가