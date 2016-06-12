from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

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
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'title',
            'user',
            'url',
        ]

    def get_user(self, obj):
        return obj.user.username

class PostDetailSerializer(ModelSerializer):
    delete_url = HyperlinkedIdentityField(
        view_name = 'posts-api:delete',
        lookup_field = 'slug',
    )

    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'user',
            'image',
            'slug',
            'content',
            'html',
            'publish',
            'delete_url',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image
