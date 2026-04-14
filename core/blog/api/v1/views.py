from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
# from blog.models import Post
from ...models import Post
from .serializers import PostSerializer


@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
# @permission_classes([IsAuthenticatedOrReadOnly])
@permission_classes([IsAdminUser])
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