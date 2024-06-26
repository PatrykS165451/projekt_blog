from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'author', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput (attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }