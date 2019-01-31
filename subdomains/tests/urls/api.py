try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url  # noqa

from subdomains.tests.urls.default import urlpatterns as default_patterns
from subdomains.tests.views import view


urlpatterns = default_patterns + [
    url(regex=r'^$', view=view, name='home'),
    url(regex=r'^view/$', view=view, name='view'),
]
