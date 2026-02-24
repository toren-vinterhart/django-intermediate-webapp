from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'published_date']



''' A test simple form
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
'''