from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from memoreminder.models import MemoUser

MEMOUSER_KEY = 'Memouser-Token'


class AllowMemoUser(BasePermission):

    def has_permission(self, request, view):
        if MEMOUSER_KEY in dict(request.headers):
            token = request.headers[MEMOUSER_KEY]
            user = MemoUser.objects.filter(token=token).first()
            if user:
                return True
        return False


class TokenModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, AllowMemoUser)

    def get_serializer_context(self):
        context = super(TokenModelViewSet, self).get_serializer_context()
        user = self.get_user()
        if self.action == 'create' or self.action == 'partial_update':
            context['user'] = user.pk
        return context

    def get_user(self):
        token = self.request.headers[MEMOUSER_KEY]
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
    permission_classes = (IsAuthenticated, AllowMemoUser)

    def get_user(self):
        token = self.request.headers[MEMOUSER_KEY]
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        return user
