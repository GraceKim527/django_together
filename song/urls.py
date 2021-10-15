from django.urls import path
import song.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', song.views.song_main, name='song_main'),
    path('song_detail/<str:id>/', song.views.song_detail, name='song_detail'),
    path('song_write/', song.views.song_write, name='song_write'),
    path('song_write/song_create/', song.views.song_create, name='song_create'),
    path('song_edit/<str:id>/', song.views.song_edit, name='song_edit'),
    path('song_delete/<str:id>/', song.views.song_delete, name='song_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)