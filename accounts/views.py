from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#from blog.serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
#   serializer_class = UserRegistrationSerializer
    
class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES