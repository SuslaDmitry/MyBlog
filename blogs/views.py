from django.shortcuts import render
from .models import BlogPost
from .forms import BlogPostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

# Create your views here.
def posts(request):
    """Домашняя страница приложения Blog выводит список постов"""
    posts = BlogPost.objects.order_by('-date_added')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    context = {'posts': page}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Добавляет новий пост."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = BlogPostForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Редактирует существующий пост."""
    post = BlogPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = BlogPostForm(instance=post)
    else:
        # Отправка данных POST; обработать данные.
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('blogs:index'))

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)