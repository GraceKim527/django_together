from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import KangBlog
from .forms import CreateForm, CommentForm
from django.http.response import HttpResponse #좋아요용

def Kang_main(request):
    blogs = KangBlog.objects
    return render(request, 'Kang/Kang_main.html', {'blogs':blogs})

def Kang_write(request):
    return render(request, 'Kang/Kang_write.html')

def Kang_create(request, blog=None):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('Kang_main')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'Kang/Kang_write.html', {'form':form})

def Kang_edit(request, id):
    blog = get_object_or_404(KangBlog, id = id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('Kang_main')
    else:
        form = CreateForm(instance=blog)
    return render(request, 'Kang/Kang_edit.html', {'form':form})

def Kang_delete(request, id):
    delete_blog = get_object_or_404(KangBlog, id = id)
    delete_blog.delete()
    return redirect ('Kang_main')

# 디테일
def Kang_detail(request, id):
    blog = get_object_or_404(KangBlog, id=id)
    default_view_count = blog.view_count
    blog.view_count = default_view_count + 1
    blog.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('Kang_detail', id)
    else:
        form = CommentForm()
        return render(request, 'Kang/Kang_detail.html', {'blog':blog, 'form':form})

#좋아요
def Kang_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    blog = get_object_or_404(KangBlog, pk=pk)
    user = request.user

    if blog.Blog_likes.filter(id=user.id).exists():
        blog.Blog_likes.remove(user)
    else:
        blog.Blog_likes.add(user)
    
    return redirect('Kang_detail', pk)