from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.


def index_view(request):
    """
    A function-based view to show index page
    """
    context = {'name': 'Sam'}
    return render(request, 'index.html', context)


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

