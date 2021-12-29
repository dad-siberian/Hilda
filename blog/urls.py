from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),         class-based views
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('newpost/', views.post_new, name='post_new'),
    path('<tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    
]
