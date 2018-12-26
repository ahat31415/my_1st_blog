from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
import datetime


def post_list(request):
    # представление для отображения постов в шаблон
    # Извлекаем посты сортируя их по дате публикации
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    now = datetime.datetime.now()
    return render(request, 'blog/post_list.html', locals())


def post_list_2h(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    now = datetime.datetime.now()
    now2 = datetime.datetime.now() + datetime.timedelta(hours=2)
    return render(request, 'blog/post_list.html', locals())


def post_detail(request, pk):
    # Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def delete_post(request, pk):
    p = get_object_or_404(Post, pk=pk)
    # p = Post.objects.get(title=pk.title)
    p.delete()
    # return render(request, 'blog/delete_post.html', {'message': 'deleted'})
    return render(request, 'blog/post_detail.html', {'del': 'deleted'})
    # else:
    #     return render(request, 'blog/delete_post.html', {'message': 'something wrong!!!'})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)  # Строим форму с данными из формы
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


