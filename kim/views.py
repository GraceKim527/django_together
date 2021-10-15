from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from .models import Gram
from .forms import CreateForm, CommentForm

# Create your views here.
def kimmain(request): #main
    blog = Gram.objects
    return render(request, 'kim/kimmain.html', {'blog':blog})

def kimnew(request):
    return render(request, 'kim/kimnew.html')

# def kimcreate(request):
#     blog = Gram()
#     blog.title = request.POST['title']
#     blog.body = request.POST['body']
#     blog.pub_date = timezone.now()
#     blog.save()
#     return redirect('kimmain')

def kimcreate(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('kimmain')
    else:
        form = CreateForm()
        return render(request, 'kim/kimnew.html', {'form': form})

def kimedit(request, id):
    edit_blog = Gram.objects.get(id=id)
    return render(request, 'kim/kimedit.html', {'blog': edit_blog})

def kimupdate(request, id):
    update_blog = Gram.objects.get(id = id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('kimmain')

def kimdelete(request, id):
    delete_blog = Gram.objects.get(id = id)
    delete_blog.delete()
    return redirect('kimmain')

def kimcomment(request, id):
    blog = get_object_or_404(Gram, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('kimmain',id)
    else:
        form = CommentForm()
        return render(request, 'kim/kimmain.html', {'blog':blog, 'form':form})    