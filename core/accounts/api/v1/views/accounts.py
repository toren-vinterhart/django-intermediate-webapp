from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from accounts.models import User
from django.core.mail import send_mail
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers import (RegistrationSerializer, 
                          CustomAuthTokenSerializer, 
                          CustomTokenObtainPairSerializer, 
                          ChangePasswordSerializer,
                          )


User = get_user_model()

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class(data=request.data)
        serializer = RegistrationSerializer(data=request.data)

        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # data = {
        #     'email': serializer.validated_data['email']
        # }
        # return Response(data, status=status.HTTP_201_CREATED)

        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
        })


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    # model = User

    def get_object(self):
        return self.request.user
        
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # if not self.object.check_password(serializer.data.get('old_password')):
            if not self.object.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.validated_data['new_password'])
            self.object.save()
            return Response({'details': 'password changed successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TestEmailSendApiView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
        return Response('The email has been sent')

