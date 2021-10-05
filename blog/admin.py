from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'author', 'published_date')
    list_filter = ('created_date', 'published_date', 'author')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['published_date']


   
  




admin.site.register(Post, PostAdmin)
