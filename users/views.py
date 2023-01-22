from .models import UserModel
from rest_framework import generics
from .serializers import UserSerializer


class UserCreationAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
