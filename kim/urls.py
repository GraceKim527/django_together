from django.urls import path
from django.urls.resolvers import URLPattern
import kim.views

urlpatterns = [
    path('', kim.views.kimmain, name='kimmain'),
]