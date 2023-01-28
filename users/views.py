from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .models import UserModel
from rest_framework import generics, views
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreationAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


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

        response = Response()
        response.set_cookie(key='refresh', value=refresh, httponly=True)

        response.data = {
            'access': str(refresh.access_token)
        }
        return response


class RefreshTokenAPIView(views.APIView):
    def get(self, request):
        refresh = RefreshToken(request.COOKIES.get('refresh'))
        return Response({'access': str(refresh.access_token)})
