# blog/serializers.py
from rest_framework import serializers
from blog.models import Post

#class UserSerializer(serializers.ModelSerializer):
    #class Meta:
    #    model = User
    #    fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
#    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user', 'created_at']
