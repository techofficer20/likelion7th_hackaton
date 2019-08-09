from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post, Comment


def postmain(request):
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    postss = paginator.get_page(page)
    return render(request, 'postmain.html', {'posts': posts, 'postss': postss, })


def post(request):
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    postss = paginator.get_page(page)
    return render(request, 'post.html', {'posts': posts, 'postss': postss, })


def result(request):
    obj_title = request.GET.get('title')
    obj_location = request.GET.get('location')
    obj_feature = request.GET.get('feature')
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    postss = paginator.get_page(page)
    return render(request, 'result.html', {'obj_title': obj_title, 'posts': posts, 'postss': postss, 'obj_location': obj_location, 'obj_feature': obj_feature})


def detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id)
    post_comment = Comment.objects.filter(post=post_id)
    return render(request, 'detail.html', {'post': detail, 'comments': post_comment, 'post_id': str(post_id)})


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
    # return redirect('/post/' + str(post.id))


def comment(request, post_id):
    if request.method == 'POST':
        # if request.user.is_authenticated:
        comment = Comment()
        comment.comment = request.POST['text']
        comment.date = timezone.datetime.now()
        comment.author = request.user
        comment.post = Post.objects.get(id=post_id)
        comment.save()
        return redirect('/detail/'+str(post_id))
        # else:
        # return redirect('signin')


def like(request, post_id):
   #post = get_object_or_404(Post, pk=post_id)
    post = Post.objects.get(pk=post_id)
    if post.user.filter(username=request.user.username).exists():
        post.user.remove(request.user)
        message = '취소하였습니다'
    else:
        post.user.add(request.user)
        message = '좋아요'
    post.save()
    context = {'like_count': post.total_likes, 'message': message}
    return redirect('detail', post_id)
