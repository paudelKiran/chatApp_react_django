from rest_framework.response import Response
from api.serializer import RegisterSerializer
from api.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer