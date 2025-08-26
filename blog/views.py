from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from blog.models import Post, Comment, Author
from blog.serializers import PostSerializer, CommentSerializer
from blog.permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        author_profile, created = Author.objects.get_or_create(user=self.request.user)
        serializer.save(author=author_profile)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorOrReadOnly]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        author_profile, created = Author.objects.get_or_create(user=self.request.user)
        serializer.save(author=author_profile)
