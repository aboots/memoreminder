from django.db.models import Count
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from memoreminder.models import Post, MemoUser
from memoreminder.serializers.post_serializer import PostSerializer
from memoreminder.views_api.token_view_set import TokenModelViewSet


class PostModelViewSet(TokenModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    do_not_filter = True

    def get_queryset(self):
        user = self.get_user()
        queryset = super(PostModelViewSet, self).get_queryset()
        ls = [user.pk]
        for friend in user.friends.all():
            ls.append(friend.pk)
        return queryset.filter(creator_user__in=ls)


class TopPostsModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(mode=Post.MODE_PUBLIC).annotate(num_likes=Count('postlike')).order_by('-num_likes')[:10]
    serializer_class = PostSerializer


class TaggedPostModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    do_not_filter = True

    def get_queryset(self):
        user = self.get_user()
        queryset = super(TaggedPostModelViewSet, self).get_queryset()
        ls = [user.pk,]
        return queryset.filter(tagged_people__in=ls)

    def get_user(self):
        token = self.request.query_params.get('token')
        if not token:
            raise PermissionDenied('user token missed')
        user = MemoUser.objects.filter(token=token).first()
        if not user:
            raise PermissionDenied('user token not found')
        return user
