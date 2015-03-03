from rest_framework import routers

from . import api


router = routers.SimpleRouter()

router.register(r'brewery', api.BreweryViewSet)
router.register(r'price', api.PriceViewSet)
router.register(r'taps', api.TapsViewSet)

urlpatterns = router.urls
