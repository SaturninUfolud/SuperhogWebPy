from django.contrib import admin

from . import models

#from .models import Article, ArticleSection, ExternalFileInfo, Creature





class ArticleSectionsInline(admin.StackedInline):
    model = models.ArticleSection
    extra = 1




class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['article_type']}),
        (None, {'fields': ['basic_description']}),
        (None, {'fields': ["gallery"]} ),
        
    ]

    inlines = [ArticleSectionsInline]

admin.site.register(models.Article,ArticleAdmin)


admin.site.register(models.ExternalFileInfo)

admin.site.register(models.Creature)

# Register your models here.
