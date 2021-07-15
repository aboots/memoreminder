from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from memoreminder.models import MemoUser


class TokenModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(TokenModelViewSet, self).get_serializer_context()
        user = self.get_user()
        if self.action == 'create':
            context['user'] = user.pk
        return context

    def get_user(self):
        token = self.request.query_params.get('token')
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        return user

    def get_queryset(self):
        query = super(TokenModelViewSet, self).get_queryset()
        if getattr(self, 'do_not_filter', False):
            return query
        field = self.get_serializer().memo_user_field_name
        user = self.get_user()
        dic = {field: user}
        return query.filter(**dic)


class TokenBaseApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_user(self):
        token = self.request.query_params.get('token')
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        return user
