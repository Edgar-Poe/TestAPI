from articles.models import Article, Comment, Vote
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'link', 'author_name', 'date']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author_name', 'date']


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ['id']
