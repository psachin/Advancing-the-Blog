from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish'
        ]

post_detail_url = HyperlinkedIdentityField(
        view_name = 'posts-api:detail',
        lookup_field = 'slug',
    )

class PostListSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            'title',
            'url',
        ]


class PostDetailSerializer(ModelSerializer):
    # delete_url = HyperlinkedIdentityField(
    #     view_name = 'posts-api:delete',
    #     lookup_field = 'slug',
    # )

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
            # 'delete_url',
        ]
