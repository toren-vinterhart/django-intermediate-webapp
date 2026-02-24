from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .models import Post
from .forms import PostForm

# Create your views here.


class IndexView(TemplateView):
    """ A class-based view for show index page """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Jack'
        context['posts'] = Post.objects.all()
        return context


class RedirectToMSN(RedirectView):
    """ A class-based view for redirect to msn """
    url = 'https://www.msn.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    """ A class-based view for posts list"""
    # model = Post # Instead of this we can use queryset or get_queryset method
    # queryset = Post.objects.all()
    # template_name = 'blog/post_list.html' # If we don't define it django use 'blog/post_list.html' as default
    context_object_name = 'posts' # default name is object_list
    paginate_by = 2
    # ordering = ['-published_date'] # it works when we use model or queryset instead of get_queryset method

    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-published_date')
        return posts
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostFormView(FormView):
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post-list')
    # success_url = '/blog/post/' # also we can use this way

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



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