from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image', 'public']
        labels = {'title': '', 'text': ''}
        widgets = {'title': forms.Textarea(attrs={'cols': 80, 'rows': 1}), 'text': forms.Textarea(attrs={'cols': 80})}

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['text']
#         labels = {'text': ''}
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}