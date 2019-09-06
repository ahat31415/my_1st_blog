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
        form = PostForm(request.POST, instance=post)  # not clear
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# ======================================================================================================================
def delete_post(request, pk):
    p = get_object_or_404(Post, pk=pk)
    p.delete()
    return redirect('/')


def delete_posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for i in posts:
        delete_post(request, pk=i.id)
    return redirect('/')


def adding_posts(request):
    for i in range(3):
        post = Post(title='Образец поста №' + str(i))
        post.text = "put on call off get out decline aspire reject deal conversely perception " \
                    "reliable kid warn pleasant colossus resolve praise necessarily rejoice prerequisite parentheses " \
                    "concordance precipitation comprehension indent suitcase those assertion wisdom snib egregious bother"
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
    #  return render(request, 'blog/post_list.html', {'posts': posts, 'now': now})
    return redirect('/')
