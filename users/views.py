from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import UserModel, Token
from rest_framework import generics, views
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreationAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginAPIView(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = UserModel.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Invalid password')

        refresh = RefreshToken.for_user(user)
        token = Token.objects.create(refresh_token=refresh)
        token.save()
        response = Response()
        response.set_cookie(key='refresh', value=refresh, httponly=True)

        response.data = {
            'access': str(refresh.access_token)
        }
        return response

    permission_classes = [AllowAny]


class RefreshTokenAPIView(views.APIView):
    def get(self, request):
        refresh = RefreshToken(request.COOKIES.get('refresh'))
        token = Token.objects.get(refresh_token=refresh)
        if token is None:
            raise AuthenticationFailed('You are not logged in')
        user = UserModel.objects.get(pk=refresh['user_id'])
        token.refresh_token = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie(key='refresh', value=token.refresh_token, httponly=True)
        response.data = {
            'access': str(refresh.access_token)
        }
        token.save()
        return response

    permission_classes = [AllowAny]


class LogoutUserAPIView(views.APIView):
    def get(self, request):
        refresh = RefreshToken(request.COOKIES.get('refresh'))
        response = Response()
        response.delete_cookie('refresh')
        token = Token.objects.get(refresh_token=refresh)
        token.delete()
        response.data = {
            'message': 'Successfully logged out'
        }
        return response
