from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('newpost/', views.post_new, name='post_new'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    
]
