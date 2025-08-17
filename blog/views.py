from rest_framework import viewsets, status, generics
from blog.models import Post, Comment
from blog.serializer import PostSerializer, CommentSerializer, UserRegistrationSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    
    authentication_classes = []
    permission_classes = []
    serializer_class = UserRegistrationSerializer
    
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class LoginView(generics.GenericAPIView):
    """
    API view to authenticate a user and return an auth token.
    """
    # Use the new LoginSerializer to provide the fields for the browsable API.
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
