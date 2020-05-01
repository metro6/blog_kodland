from django.shortcuts import render
from apps.articles.models import Article


def main(request):
  head_text = 'Блог'
  template = 'index.pug'
  articles = Article.objects.order_by('-created_on')[:10]
  res_articles = []

  for article in articles:
    res_articles.append({
      'true_article': '1',
      'article_info': article
    })

  for _ in range(0, 10 - len(res_articles)):
    res_articles.append({
      'true_article': 0
    })

  return render(request, template, {
    'head_text': head_text,
    'res_articles': res_articles
  })


def add_article(request):
  head_text = 'Блог / Добавить статью'
  template = 'add_article.pug'

  return render(request, template, {
    'head_text': head_text
  })