from rest_framework import routers

from .views import ShoeViewSet


router = routers.SimpleRouter()
router.register(r'shoes', ShoeViewSet)
urlpatterns = router.urls
app_name = 'core'
