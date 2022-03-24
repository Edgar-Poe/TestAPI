from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    author_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def votes(self):
        return len(Vote.objects.filter(article__id=self.id))

    def comments(self):
        return len(Comment.objects.filter(article__id=self.id))



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now=True)


class Vote(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
