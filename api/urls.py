from django.urls import include, path
from rest_framework import routers
from api.views import MealViewSet, RatingViewSet

router = routers.DefaultRouter()

router.register(r'meals', MealViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]