from rest_framework import serializers

from myapp.models import Comment, Favorite, Product
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    initiator = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    tags = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'initiator', 'title', 'slug', 'content', 'video', 'tags')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    product = ProductSerializer()

    class Meta:
        model = Favorite
        fields = ('id', 'user', 'product')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    product = ProductSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'product', 'content')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image', 'username', 'first_name', 'email')
