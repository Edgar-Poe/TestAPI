from django.urls import path
from .api import ArticleCreateApi, ArticleApi, ArticleUpdateApi, ArticleDeleteApi
from .api import CommentCreateApi, CommentApi, CommentUpdateApi, CommentDeleteApi
from .api import VoteCreateApi



urlpatterns = [
    path('',ArticleApi.as_view()),
    path('create',ArticleCreateApi.as_view()),
    path('<int:pk>',ArticleUpdateApi.as_view()),
    path('<int:pk>/delete',ArticleDeleteApi.as_view()),
    path('<article_id>/comments', CommentApi.as_view()),
    path('<article_id>/comments/create', CommentCreateApi.as_view()),
    path('<article_id>/comments/<int:pk>', CommentUpdateApi.as_view()),
    path('<article_id>/comments/<int:pk>/delete', CommentDeleteApi.as_view()),
    path('<article_id>/upvote', VoteCreateApi.as_view()),

]