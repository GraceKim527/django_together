from django.urls import path
import song.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('', song.views.song_main, name='song_main'),
    path('song_read/', song.views.song_read, name='song_read'),
    path('song_detail/<str:id>/', song.views.song_detail, name='song_detail'),
    path('song_write/', song.views.song_write, name='song_write'),
    path('song_write/song_create/', song.views.song_create, name='song_create'),
    path('song_edit/<str:id>/', song.views.song_edit, name='song_edit'),
    path('song_delete/<str:id>/', song.views.song_delete, name='song_delete'),
    path('song/song_hashtag/', song.views.hashtagform, name = 'song_hashtag'),
    path('song/<int:hashtag_id>/song_search/', song.views.song_search, name='song_search'),
    path('song_like/<int:pk>', song.views.song_like, name='song_like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)