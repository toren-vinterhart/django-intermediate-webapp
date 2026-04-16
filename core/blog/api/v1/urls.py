from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from . import views

app_name = 'api-v1'

router = DefaultRouter()
# router = SimpleRouter() # has not API root page
# router.register('post', views.PostViewSet, basename='post')
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls

# urlpatterns = [
    # path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/', views.postList, name='post-list'),
    # path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    # path('post/<int:id>/', views.postDetail, name='post-detail'),
    # path('post/', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    # path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),
    # path('', include('router.urls')),
# ]

# urlpatterns += router.urls