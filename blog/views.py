from rest_framework import viewsets, status, generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from blog.models import Post, Comment, Author
from blog.serializer import PostSerializer, CommentSerializer, UserRegistrationSerializer, LoginSerializer
from blog.permissions import IsAuthor
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    
    def get_permissions(self):
        
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthor]
        return[permission() for permission in self.permission_classes]
            
    
    def perform_create(self, serializer):
        author_profile, created = Author.objects.get_or_create(user=self.request.user)
        serializer.save(author=author_profile)
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthor]
            
        return[permission() for permission in self.permission_classes]

class UserRegistrationView(generics.CreateAPIView):
    
    authentication_classes = []
    permission_classes = []
    serializer_class = UserRegistrationSerializer
    
    queryset = User.objects.all()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
