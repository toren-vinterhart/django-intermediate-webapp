from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/', views.postList, name='post-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    # path('post/<int:id>/', views.postDetail, name='post-detail'),
]