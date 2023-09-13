from rest_framework.routers import SimpleRouter

from .views import LkappDemoModelViewSet

router = SimpleRouter()
router.register("api/lkapp", LkappDemoModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls