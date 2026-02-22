from django.urls import path
# from django.views.generic import TemplateView, RedirectView
from . import views

app_name = 'blog'

urlpatterns = [
    path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-msn/<int:pk>', views.RedirectToMSN.as_view(), name='redirect-to-msn'),
    # path('fbv-index/', views.index_view, name='fbv-index'),
    # path('go-to-msn', views.redirect_to_msn, name='redirect-to-msn'),
    # path('cbv-index/', TemplateView.as_view(template_name='index.html', extra_context={'name': 'John'}), name='cbv_index'),
    # path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index', permanent=True), name='redirect-to-index'),
    # path('go-to-msn', RedirectView.as_view(url='https://www.msn.com'), name='redirect-to-msn'),
]
