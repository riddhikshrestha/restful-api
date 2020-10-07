from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

from .models import User

# Create your views here.

@api_view(['GET'])
def apiview(request):
    api_urls = {
        'List' : '/userlist/',
        'Detail' : '/userdetail/<str:pk>/',
        'Create' : '/usercreate/',
        'Update' : '/userupdate/<str:pk>/',
        'Delete' : '/userdelete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def userlist(request):
    users = User.objects.all().order_by('-id')
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetail(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def usercreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def userupdate(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

@api_view(['DELETE'])
def userdelete(request,pk):
    user = User.objects.get(id=pk)
    
    user.delete()

    return Response("Deleted successfully") 