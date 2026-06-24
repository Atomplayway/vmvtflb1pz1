from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.order_by('-published_at')[:10]
    return render(request, 'articles/article_list.html', {'articles': articles})
