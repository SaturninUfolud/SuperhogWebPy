from django.contrib import admin

from .models import Article, ArticleSection, ExternalFileInfo





class ArticleSectionsInline(admin.StackedInline):
    model = ArticleSection
    extra = 1




class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['article_type']}),
        (None, {'fields': ['basic_description']}),
        (None, {'fields': ["gallery"]} ),
        
    ]

    inlines = [ArticleSectionsInline]

admin.site.register(Article,ArticleAdmin)


admin.site.register(ExternalFileInfo)

# Register your models here.
