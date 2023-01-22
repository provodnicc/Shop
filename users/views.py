from rest_framework import generics
from .models import UserModel
from .serializers import UserSerializer


class UserCreationAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
