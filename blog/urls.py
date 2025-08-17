from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CommentViewSet, UserRegistrationView, LoginView

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')

router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('', include(router.urls)),
]
