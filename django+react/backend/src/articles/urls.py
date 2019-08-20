from django.urls import path, include
from .views import article_list_views, article_detail_views

urlpatterns = [
    path('', article_list_views.as_view(), name='list'),
    path('<pk>/', article_detail_views.as_view(), name='details'),
]
