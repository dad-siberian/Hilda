from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(label='Текст',
                        widget=forms.Textarea(attrs={'placeholder': "What's happening?"})
                        )
    tags = forms.CharField(required=False, label='Тег')

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')





class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')