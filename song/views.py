from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import S_Blog, Song_hashtag
from .forms import CreateForm, CommentForm, HashtagForm
from django.http.response import HttpResponse

# Create your views here.

def song_main(request):
    blogs = S_Blog.objects
    hashtags = Song_hashtag.objects
    return render(request, 'song/song_main.html', {'blogs': blogs, 'hashtags':hashtags})

def song_write(request):
    return render(request, 'song/song_write.html')

def song_read(request):
    blogs = S_Blog.objects
    return render(request, 'song/song_read.html', {'blogs': blogs})

def song_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('song_read')
    else:
        form = CreateForm
        return render(request, 'song/song_write.html', {'form':form})

def song_edit(request, id):
    blog = get_object_or_404(S_Blog, id = id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('song_read')
    else:
        form = CreateForm
        return render(request, 'song/song_edit.html', {'form':form})

def song_delete(request, id):
    delete_blog = get_object_or_404(S_Blog, id = id)
    delete_blog.delete()
    return redirect ('song_read')

def song_detail(request, id):
    blog = get_object_or_404(S_Blog, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            form.save_m2m()
            return redirect('song_detail', id)
    else:
        form = CommentForm()
        return render(request, 'song/song_detail.html', {'blog':blog, 'form':form})

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Song_hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'song/song_hashtag.html', {'form':form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('song_main')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'song/song_hashtag.html', {'form':form})

def song_search(request, hashtag_id):
    hashtag = get_object_or_404(Song_hashtag, pk=hashtag_id)
    return render(request, 'song/song_search.html', {'hashtag':hashtag})

def song_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn Please')

    post = get_object_or_404(S_Blog, pk=pk)
    user = request.user

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('song_main')