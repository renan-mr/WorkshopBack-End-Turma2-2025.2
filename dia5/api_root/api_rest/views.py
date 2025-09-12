from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import requests

# Create your views here.

# criar e listar usuarios
class UserListCreateApiView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
   
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# buscar, atualizar e deletar usuarios por id

class UserDetailApiview(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
    
    def get(self,request,pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# criar usuarios pela api randomuser

class RandomUserCreateApiView(APIView):
    def post(self, request):
        try:
            response = requests.get('https://randomuser.me/api/', timeout=5)
            data = response.json()
            random_user = data ['results'][0]

            new_user = {
                'user_nickname': random_user['login']['username'],
                'user_name': f"{random_user['name']['first']} {random_user['name']['last']}",
                'user_email': random_user['email'],
                'user_age': random_user['dob']['age'],
                'user_birthdate': random_user['dob']['date'].split('T')[0],

            }

            serializer = UserSerializer(data=new_user)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
