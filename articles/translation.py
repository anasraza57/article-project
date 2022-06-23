from modeltranslation.translator import register, TranslationOptions

from articles.models import Article, Tag


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content', 'created', 'updated')


@register(Tag)
class TaggitTranslations(TranslationOptions):
    fields = ('name',)
