from django.urls import path
from rest_framework.routers import DefaultRouter

from memoreminder import views_api

router = DefaultRouter()

router.register('memo-user', views_api.MemoUserModelViewSet)
router.register('tag', views_api.TagModelViewSet)
router.register('friend-request', views_api.FriendRequestModelViewSet)
router.register('post', views_api.PostModelViewSet)
router.register('post-file', views_api.PostFileModelViewSet)
router.register('post-like', views_api.PostLikeModelViewSet)
router.register('comment-like', views_api.CommentLikeModelViewSet)
router.register('comment', views_api.CommentModelViewSet)
router.register('top-post', views_api.TopPostsModelViewSet)


urlpatterns = [
    path('login/', views_api.LoginView.as_view()),
    path('logout/', views_api.LogoutView.as_view()),
]

urlpatterns += router.urls
