from django.contrib import admin
from blog.models import Post, Comment, Author

admin.site.register(Author)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')
    list_filter = ('created_at', 'author',)
    search_fields = ('title', 'content',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'post')
    list_filter = ('created_at',)
    search_fields = ('content',)