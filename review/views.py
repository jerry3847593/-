from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    posts = Post.objects
    return render(request, 'review/home.html', {'posts':posts})

@login_required
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'review/detail.html',{'post':post_detail})

@login_required
def post_new(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:            
        form=PostForm()
    return render(request, 'review/post_new.html',{'form':form})
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk= post_id)
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.datetime.now()
            post.save()
            return redirect('detail', post_id=post.pk)
    else:            
        form=PostForm(instance=post)
    return render(request, 'review/post_edit.html',{'form':form})
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')