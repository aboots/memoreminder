from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from memoreminder.filters.memo_user_filter import MemoUserFilter
from memoreminder.models import MemoUser
from memoreminder.serializers import MemoUserSerializer
from memoreminder.serializers.user_serializer import ListMemoUserSerializer


class MemoUserModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = MemoUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MemoUserFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return ListMemoUserSerializer
        return MemoUserSerializer
