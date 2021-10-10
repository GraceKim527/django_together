from django.shortcuts import render

# Create your views here.
def kimmain(request):
    return render(request, 'kim/kimmain.html')