from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from .models import *

# Create your views here.


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = (TokenAuthentication,)