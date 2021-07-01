from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from memoreminder.models import MemoUser
from memoreminder.serializers import MemoUserSerializer


class MemoUserModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = MemoUser.objects.all()
    serializer_class = MemoUserSerializer
