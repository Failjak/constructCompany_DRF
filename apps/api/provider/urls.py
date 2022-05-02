from rest_framework.routers import SimpleRouter

from .views import ProviderView


router = SimpleRouter()
router.register('', ProviderView, basename='provider')

urlpatterns = router.urls
