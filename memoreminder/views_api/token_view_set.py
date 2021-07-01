from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from memoreminder.models import MemoUser


class TokenModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(TokenModelViewSet, self).get_serializer_context()
        token = self.request.query_params.get('token')
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        context['user'] = user.pk
        return context
