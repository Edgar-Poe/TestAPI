from rest_framework import generics
from articles.models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, VoteSerializer


class ArticleCreateApi(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleApi(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDeleteApi(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentCreateApi(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        article_id = self.kwargs['article_id']
        serializer.save(article=Article.objects.get(pk=article_id))


class CommentApi(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.filter(article__id=article_id)


class CommentUpdateApi(generics.RetrieveUpdateAPIView):
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        article_id = self.kwargs['article_id']
        serializer.save(article=Article.objects.get(pk=article_id))

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.filter(article__id=article_id)


class CommentDeleteApi(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.filter(article__id=article_id)


class VoteCreateApi(generics.CreateAPIView):
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        article_id = self.kwargs['article_id']
        serializer.save(article=Article.objects.get(pk=article_id))
