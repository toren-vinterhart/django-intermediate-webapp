# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.decorators import (
#     api_view,
#     action,
#     permission_classes,
# )
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    # IsAdminUser,
)
from rest_framework import (
    # mixins,
    # generics,
    viewsets,
)

# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# from blog.models import Post
from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer

# from .permissions import IsOwnerOrReadOnly
from .paginations import DefaultPagination

# region function_base_api_view
"""
@api_view(["GET", "POST"])
# @permission_classes([IsAdminUser])
# @permission_classes([IsAuthenticatedOrReadOnly])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True).order_by('-published_date')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail': 'Item removed successfully!!!'}, status=status.HTTP_204_NO_CONTENT)


    # We can do this if we don't want to use get_object_or_404 function
    # try:
    #     post = Post.objects.get(pk=id)
    #     # print(post.__dict__)
    #     serializer = PostSerializer(post)
    #     # print(serializer.__dict__)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     # return Response({'detail': 'post does not exists'}, status=404)
    #     return Response({'detail': 'post does not exists'}, status=status.HTTP_404_NOT_FOUND)
"""
# endregion


# region class_base_API_View
'''
class PostList(APIView):
    """ Getting a list of posts and creating new posts """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """ retriveing a list of posts """
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ creating a post with provided data """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ retriveing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ editing the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """ deleting the post object """
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail': 'Item removed successfully!!!'}, status=status.HTTP_204_NO_CONTENT)
'''
# endregion


# region class_base_Mixin_and_Generic_API_View
"""
class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""
# endregion


# region class_base_generics_API_View
"""
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    # lookup_field = 'id' # If we use id in urls instead of pk we must set this
"""
# endregion


# region class_base_ViewSets_API_View
"""
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer

    def list(self, request):
        query = Post.objects.filter(status=True) # use this query in this line because global queryset didn't update after editing or deleting until restart app.
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        post_object.delete()
        return Response({'detail': 'Item deleted successfully!!!'}, status=status.HTTP_204_NO_CONTENT)
"""
# endregion


# region class_base_ModelViewSets_API_View


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [
        # IsAuthenticated,
        # IsOwnerOrReadOnly,
        IsAuthenticatedOrReadOnly,
    ]
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    pagination_class = DefaultPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # filterset_fields = ['category', 'author', 'status']
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["created_date", "published_date"]

    # A custom action
    # @action(methods=['get'], detail=False) # detail must be True if we have args like pk.
    # def get_ok(self, request):
    #     return Response({'detail': 'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# endregion
