from rest_framework.routers import SimpleRouter

from .views import MaterialView


router = SimpleRouter()
router.register('', MaterialView, basename='material')

urlpatterns = router.urls
