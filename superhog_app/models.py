from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 60)
    publication_date = models.DateTimeField(auto_now_add=True, blank=True)
    basic_description = models.TextField(default="")

    def __str__(self):
        return self.title



class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length = 60)
    content = models.TextField(default="")

    def __str__(self):
        return self.title