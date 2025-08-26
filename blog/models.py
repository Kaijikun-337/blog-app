from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.user.username} on {self.post.title}'

    class Meta:
        ordering = ['-created_at']

@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'author'):
        Author.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_author_profile(sender, instance, **kwargs):
    if hasattr(instance, 'author'):
        instance.author.save()
