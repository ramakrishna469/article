from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
       'article.views',
       url(r'^add_article/$', 'add_article', name="add_article"),
       url(r'^$', 'article_list', name="article_list"),
       )
# (?P<name>[a-zA-Z0-9_-]+)