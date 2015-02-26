from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from . import api


brewery_urls = [
    url(r'^/?$', api.BreweryListCreate.as_view())
]

taps_urls = [
    url(r'^/create/?$', api.TapsCreate.as_view(), name='taps.create'),
    url(r'^/(?P<pk>\d+)/?$', api.TapsDetail.as_view(), name='taps.detail'),
    url(r'^/?$', api.TapsList.as_view(), name='taps.list'),
]

urlpatterns = [
    url(r'^brewery', include(brewery_urls)),
    url(r'^taps', include(taps_urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
