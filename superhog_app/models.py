from django.db import models

# Create your models here.


class ExternalFileInfo(models.Model):
    PICTURE = 0
    VIDEO_MP4 = 1
    TEXT = 2
    SOURCE_CODE = 3
    OTHER = 4

    FILE_TYPE_CHOICES = [
        (0, "Picture"),
        (1, "Video"),
        (2, "Text"),
        (3, "Source code"),
        (4, "Other"),
    ]

    filetype = models.SmallIntegerField(choices = FILE_TYPE_CHOICES, default=PICTURE)
    description = models.CharField(max_length = 45, default ="")
    internal_path = models.CharField(max_length = 256)

    def __str__(self):
        if self.description is None or self.description == "":
            return self.internal_path

        else:
            return self.internal_path + " (" + self.description +")"

    @property
    def get_url(self):
        return "sh_app/" + self.internal_path


class Article(models.Model):
    
    SH_MISC = 0
    SH_GAMEPLAY = 1
    SH_CREATURE = 2
    SH_SOURCE_CODE = 3

    OTHER = 10

    ARTICLE_TYPE_CHOICES = [
        (0, "Superhog różne"),
        (1, "Superhog rozgrywka"),
        (2, "Superhog potwory"),
        (3, "Superhog kod źródłowy"),
        (10, "Inne programy"),
    ]
    
    title = models.CharField(max_length = 60)
    publication_date = models.DateTimeField(auto_now_add=True, blank=True)
    basic_description = models.TextField(default="")
    gallery = models.ManyToManyField(ExternalFileInfo)

    article_type = models.SmallIntegerField(choices=ARTICLE_TYPE_CHOICES, default=SH_MISC)

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length = 60)
    content = models.TextField(default="")

    def __str__(self):
        return self.title

class Creature(models.Model):

    genus = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    feed = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.genus.rstrip()+" "+self.species.rstrip()