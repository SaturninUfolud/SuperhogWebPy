from django.contrib import admin

from .models import Article, ArticleSection


class ArticleSectionsInline(admin.StackedInline):
    model = ArticleSection
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]

    inlines = [ArticleSectionsInline]

admin.site.register(Article,ArticleAdmin)


# Register your models here.
