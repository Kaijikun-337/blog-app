from rest_framework import serializers
from blog.models import Post, Comment, Author
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'username']

class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']
        
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments']
        read_only_fields = ['created_at']

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)