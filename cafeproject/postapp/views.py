from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post, Comment


def post(request):
    posts = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    postss = paginator.get_page(page)
    return render(request, 'post.html', {'posts': posts, 'postss': postss, })


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
