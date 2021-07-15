from django.urls import path
from rest_framework.routers import DefaultRouter

from memoreminder import views_api

router = DefaultRouter()

router.register('memo-user', views_api.MemoUserModelViewSet)
router.register('tag', views_api.TagModelViewSet)
router.register('friend-request', views_api.FriendRequestModelViewSet)
router.register('post', views_api.PostModelViewSet)
router.register('post_file', views_api.PostFileModelViewSet)


urlpatterns = [
    path('login/', views_api.LoginView.as_view()),
    path('logout/', views_api.LogoutView.as_view()),
]

urlpatterns += router.urls
