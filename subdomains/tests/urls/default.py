try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url  # noqa

from subdomains.tests.views import view


urlpatterns = [
    url(regex=r'^$', view=view, name='home'),
    url(regex=r'^example/$', view=view, name='example'),
]
