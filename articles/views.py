from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from articles.models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/home.html', context)


def detail(request, slug):
    languages = dict(settings.LANGUAGES).keys()
    q = Q()
    for lang in languages:
        kwargs = {'slug_%s' % lang: slug}
        q |= Q(**kwargs)
    articles = Article.objects.filter(q)
    if articles.exists():
        article = articles.first()
        context = {
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    else:
        return Http404

