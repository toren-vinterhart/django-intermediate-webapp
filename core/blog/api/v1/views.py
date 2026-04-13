from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post


@api_view()
def postList(request):
    return Response("Hi, this is a testing API")


@api_view()
def postDetail(request, id):
    # post = get_object_or_404(Post, id=id)
    return Response({'post': 'post', 'id': id})