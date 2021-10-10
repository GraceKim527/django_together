from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Kang_main, name='Kang_main'),
    path('Kang_detail/<str:id>/', views.Kang_detail, name='Kang_detail'),
    path('Kang_write/', views.Kang_write, name='Kang_write'),
    path('Kang_write/Kang_create/', views.Kang_create, name='Kang_create'),
    path('Kang_edit/<str:id>/', views.Kang_edit, name='Kang_edit'),
    path('Kang_delete/<str:id>/', views.Kang_delete, name='Kang_delete'),
    path('Kang_like/<int:pk>', views.Kang_like, name='Kang_like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
