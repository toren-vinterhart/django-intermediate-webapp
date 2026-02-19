from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    path('fbv-index/', views.indexView, name='fbv_index'),
    path('cbv-index/', TemplateView.as_view(template_name='index.html', extra_context={'name': 'John'}), name='cbv_index'),
]