try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url  # noqa

from subdomains.tests.urls.default import urlpatterns as default_patterns


urlpatterns = default_patterns
