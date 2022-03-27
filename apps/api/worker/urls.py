from rest_framework.routers import SimpleRouter

from .views import WorkerView


router = SimpleRouter()
router.register('', WorkerView, basename='worker')

urlpatterns = router.urls
