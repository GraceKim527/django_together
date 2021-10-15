from django.urls import path
from django.urls.resolvers import URLPattern
import kim.views

urlpatterns = [
    path('', kim.views.kimmain, name = 'kimmain'),
    # path('new/', kim.views.kimnew, name='kimnew'),
    path('new/create/', kim.views.kimcreate, name = 'kimcreate'),
    path('edit/<str:id>', kim.views.kimedit, name = 'kimedit'),
    path('update/<str:id>', kim.views.kimupdate, name = 'kimupdate'),
    path('delete/<str:id>', kim.views.kimdelete, name = 'kimdelete'),
    path('comment/<str:id>', kim.views.kimcomment, name = 'kimcomment'),
]