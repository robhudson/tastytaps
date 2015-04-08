from rest_framework import routers

from . import api


router = routers.SimpleRouter()
router.register(r'taps', api.TapsViewSet)


urlpatterns = router.urls
