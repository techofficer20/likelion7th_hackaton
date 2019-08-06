from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

def post(request):
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    postss = paginator.get_page(page)
    return render(request, 'post.html', {'posts': posts, 'postss':postss})

def detail(request, post_id):
    detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'post': detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    post = Post()
    post.title = request.POST['title']
    post.image = request.FILES['image']
    post.date = timezone.datetime.now()
    post.body = request.POST['body']
    post.area = request.POST['area']
    post.save()
    return redirect('/post')
    #return redirect('/post/' + str(post.id))
