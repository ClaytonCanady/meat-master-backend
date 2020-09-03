from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description',
                  'ingredients', 'instructions', 'photo_url', 'author')
