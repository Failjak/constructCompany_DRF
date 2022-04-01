from rest_framework.routers import SimpleRouter

from .views import ItemView


router = SimpleRouter()
router.register('', ItemView, basename='item')

urlpatterns = router.urls
