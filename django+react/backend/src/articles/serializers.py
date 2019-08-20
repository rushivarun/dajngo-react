from rest_framework import serializers
from .models import articles


class article_serializer(serializers.ModelSerializer):
    class Meta:
        model = articles
        fields = ('title', 'content', 'created_by', 'id')
