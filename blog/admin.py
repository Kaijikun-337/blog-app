from django.contrib import admin
from blog.models import Post

#class CommentInline(admin.StackedInline):
    #model = Comment
    #extra = 1
    
class PostAdmin(admin.ModelAdmin):
#    inlines = [CommentInline]
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content',)
    

#admin.site.register(Author)
admin.site.register(Post, PostAdmin)