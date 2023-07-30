from django.urls import include, path
from rest_framework.authtoken import views 

from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostViewSet, FollowViewSet, GroupViewSet

app_name = 'api'

router = DefaultRouter() 

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
router.register( 
    'posts/(?P<post_id>[^/.]+)/comments', 
    CommentViewSet, 
    basename='comments'
)

urlpatterns = [ 
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
] 
