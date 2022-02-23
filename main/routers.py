from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'map', views.MapImageViewSet, basename='map')