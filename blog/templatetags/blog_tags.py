from django import template
from django.utils import timezone
from django.db.models import Count
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.filter(published_date__lte=timezone.now()).count()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(published_date__lte=timezone.now())[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments'))[:count]
