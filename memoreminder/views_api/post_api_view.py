from memoreminder.models import Tag, Post
from memoreminder.serializers import TagSerializer
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

