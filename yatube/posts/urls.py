from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='groups'),
    path('', views.index, name='main'),
]
