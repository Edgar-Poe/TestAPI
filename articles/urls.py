from django.urls import path
from articles import views




urlpatterns = [
    path('', views.articles_list, name='news'),
    path('article/<int:art_id>/', views.single_article, name='Comments'),
]