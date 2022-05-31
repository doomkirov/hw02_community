from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('group/slug:slug', include('posts.urls', namespace='groups')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
]
