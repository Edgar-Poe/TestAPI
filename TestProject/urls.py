from django.urls import path, include


urlpatterns = [
    path('', include('articles.urls')),
    path('api/', include('api.urls')),
]

