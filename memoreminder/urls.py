from django.urls import path
from rest_framework.routers import DefaultRouter

from memoreminder import views_api

router = DefaultRouter()

router.register('memo-user', views_api.MemoUserModelViewSet)
router.register('tag', views_api.TagModelViewSet)
router.register('friend-request', views_api.FriendRequestModelViewSet)


urlpatterns = [
    path('login/', views_api.LoginView.as_view()),
]

urlpatterns += router.urls
