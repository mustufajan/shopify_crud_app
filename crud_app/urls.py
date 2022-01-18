from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, InventoryCollectionViewSet

router = DefaultRouter()

router.register(r"api/inventory_item", InventoryItemViewSet, basename="inventory_item")

router.register(
    r"api/inventory_collection",
    InventoryCollectionViewSet,
    basename="inventory_collection",
)


urlpatterns = [
    re_path(r"^", include(router.urls)),
]
