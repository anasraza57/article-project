from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from articles.models import Article


# Register your models here.
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'content_en', 'content_de')
    search_fields = ('tags__name',)


admin.site.register(Article, ArticleAdmin)
