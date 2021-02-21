from django.db import models

# Create your models here.


class ExternalFileInfo(models.Model):
    PICTURE = 0,
    VIDEO_MP4 = 1,
    TEXT = 2,
    SOURCE_CODE = 3,
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