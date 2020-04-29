from django.conf.urls import url

from .views import *

app_name = 'articles'
urlpatterns = [
    url(r'^create/$', ArticleCreateView.as_view()),
    url(r'^all/$', ArticleListView.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', ArticleUpdateDestroyView.as_view()),
]