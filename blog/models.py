from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from pytils import translit
from taggit.managers import TaggableManager

# Посты блога
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = TaggableManager()



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.slug])

        
# переопределение функции save() для создания слизня с использованием pytils для транслитизации кириллицы
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translit.slugify(self.title)
        return super().save(*args, **kwargs)

#  Коментарии
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


# class Meta:
#     ordering = ('-publish',)
