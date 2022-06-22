import taggit.models
from modeltranslation.translator import register, TranslationOptions

from articles.models import Article


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content', 'created', 'updated')


@register(taggit.models.Tag)
class TaggitTranslations(TranslationOptions):
    fields = ('name',)
