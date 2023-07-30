from rest_framework import viewsets, permissions
from django.core.exceptions import PermissionDenied
from posts.models import Comment, Post, Group, Follow
from django.shortcuts import get_object_or_404
from .serializers import CommentSerializer, PostSerializer, GroupSerializer, FollowSerializer
from rest_framework.pagination import LimitOffsetPagination

class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer): 
        serializer.save(author=self.request.user) 

    def perform_update(self, serializer): 
        if serializer.instance.author != self.request.user: 
            raise PermissionDenied('Изменение чужого контента запрещено!') 
        serializer.save(author=self.request.user) 

 
    def perform_destroy(self, instance): 
        if instance.author != self.request.user: 
            raise PermissionDenied('Изменение чужого контента запрещено!') 
        instance.delete() 


class CommentViewSet(viewsets.ModelViewSet): 
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer 

    def get_queryset(self): 
        post_id = self.kwargs.get('post_id') 
        post = get_object_or_404(Post, id=post_id) 
        return post.comments.all() 

    def perform_create(self, serializer): 
        post_id = self.kwargs.get('post_id') 
        post = get_object_or_404(Post, id=post_id) 
        serializer.save( 
            post=post, author=self.request.user 
        ) 


    def perform_update(self, serializer): 
        if serializer.instance.author != self.request.user: 
            raise PermissionDenied('Изменение чужого контента запрещено!') 
        serializer.save(author=self.request.user) 
 
    def perform_destroy(self, instance): 
        if instance.author != self.request.user: 
            raise PermissionDenied('Изменение чужого контента запрещено!') 
        instance.delete()

class GroupViewSet(viewsets.ReadOnlyModelViewSet): 

    queryset = Group.objects.all() 
    serializer_class = GroupSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer