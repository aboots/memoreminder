from django.urls import path
from rest_framework.routers import DefaultRouter

from memoreminder import views_api

router = DefaultRouter()

router.register('memo-user', views_api.MemoUserModelViewSet)


urlpatterns = [
]

urlpatterns += router.urls
