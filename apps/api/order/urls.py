from rest_framework.routers import SimpleRouter

from .views import OrderView


router = SimpleRouter()
router.register('', OrderView, basename='order')

urlpatterns = router.urls
