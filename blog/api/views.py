from blog.api.serializers import PostSerialiser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from django.contrib.auth.models import User


@api_view(['GET', ])
def api_detail_blog_view(request,slug):
    try:
        post=Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

    if request.method=='GET':
        serializer=PostSerialiser(post)
        return Response(serializer.data)

@api_view(['PUT', ])
def api_update_blog_view(request,slug):
    try:
        post=Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

    if request.method=='PUT':
        serializer=PostSerialiser(post,data=request.data)
        data={}
        if serializer.is_valid:
            serializer.save()
            data['success']='update successful'
            return Response(data=data)
        return Response(serializer.error,status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_blog_view(request,slug):
    try:
        post=Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    

    if request.method=='DELETE':
        operation=post.delete()
        data={}
        if operation:
            data['success']='delete successful'
        else:
            data['failure']='delete failure'
        return Response(data=data)
  





@api_view(['POST', ])
def api_create_blog_view(request):
    acct=User.objects.get(pk=1)

    post=Post(author=acct)

    if request.method=='POST':
        serial=PostSerialiser(post,data=request.data)
        if serial.is_valid:
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
