from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, UserProfileSerializer
from rest_framework.generics import get_object_or_404
from users.models import User

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
# Create your views here.


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'가입완료'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_class = [permissions.IsAuthenticated]
    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response('get 요청')
    

class FollowView(APIView):
    def post(self, request, user_id):
        user_you = get_object_or_404(User, id=user_id)
        user_me = request.user

        if user_me in user_you.followers.all():
            user_you.followers.remove(request.user) #요청 유저가 없으면 제거
            return Response("unfollow 했습니다", status=status.HTTP_200_OK)
        else:
            user_you.followers.add(request.user) #요청 유저가 없으면 추가
            return Response("follow 완료!", status=status.HTTP_200_OK)


class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)