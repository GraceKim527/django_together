from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import S_Blog
from .forms import CreateForm, CommentForm

# Create your views here.

def song_main(request):
    blogs = S_Blog.objects
    return render(request, 'song/song_main.html', {'blogs': blogs})

def song_write(request):
    return render(request, 'song/song_write.html')

def song_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('song_main')
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
            return redirect('song_main')
    else:
        form = CreateForm
        return render(request, 'song/song_edit.html', {'form':form})

def song_delete(request, id):
    delete_blog = get_object_or_404(S_Blog, id = id)
    delete_blog.delete()
    return redirect ('song_main')

def song_detail(request, id):
    blog = get_object_or_404(S_Blog, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('song_detail', id)
    else:
        form = CommentForm()
        return render(request, 'song/song_detail.html', {'blog':blog, 'form':form})