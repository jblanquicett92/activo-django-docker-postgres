from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import UserSerializer, AuthTokenSerializer



class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UsuarioLatLngView(GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        return Response({'status':'post'})
    
    def get(self, request):
        return Response({'status':'get'})