from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm, ProfileForm
from .models import Post, Profile

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})  

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
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

def profile(request):
    profile = get_object_or_404(Profile)
    return render(request, 'blog/profile.html',{'profile': profile})

def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk = 1)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=post)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('profile', pk = 1)
    else:
        form = ProfileForm(instance = profile)
    return render(request, 'blog/profile/profile_edit.html',{'profile' : profile})
