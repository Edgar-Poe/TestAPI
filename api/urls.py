from django.urls import path
from .views import ArticleCreateApi, ArticleApi, ArticleUpdateApi, ArticleDeleteApi
from .views import CommentCreateApi, CommentApi, CommentUpdateApi, CommentDeleteApi
from .views import VoteCreateApi



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