from django.contrib import admin
from blog.models import Post, Comment, Author

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'created_at', 'author')
    list_filter = ('created_at', 'author',)
    search_fields = ('title', 'content',)
    

admin.site.register(Author)
admin.site.register(Post, PostAdmin)