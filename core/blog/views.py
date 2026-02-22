from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from .models import Post

# Create your views here.


class IndexView(TemplateView):
    """
    A class-based view for show index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Jack'
        context['posts'] = Post.objects.all()
        return context


class RedirectToMSN(RedirectView):
    """A class-based view for redirect to msn"""
    url = 'https://www.msn.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)

    
''' FBV to show a template
def index_view(request):
    """
    A function-based view to show index page
    """
    context = {'name': 'Sam'}
    return render(request, 'index.html', context)
'''


''' FBV for redirect
def redirect_to_msn(request):
    return redirect('https://www.msn.com')
'''