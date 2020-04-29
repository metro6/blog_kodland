from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ArticleConfig(AppConfig):
    name = 'apps.articles'
    verbose_name = _('Articles')
