from django.shortcuts import render
from .serializers import article_serializer
from rest_framework.viewsets import generics
from .models import articles


class article_list_views(generics.ListAPIView):
    queryset = articles.objects.all()
    serializer_class = article_serializer


class article_detail_views(generics.RetrieveAPIView):
    queryset = articles.objects.all()
    serializer_class = article_serializer
