from django import forms
from .models import Post


class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'status', 'category', 'published_date']



''' A test simple form
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
'''