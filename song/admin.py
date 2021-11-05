from django.contrib import admin
from .models import S_Blog, Song_comment, Song_hashtag

# Register your models here.

admin.site.register(S_Blog)
admin.site.register(Song_comment)
admin.site.register(Song_hashtag)