from rest_framework import routers
from django.urls import path

from .api import (
    ItemViewSet,
    UserViewSet,
    ColorViewSet,
    PackagingViewSet,
    OrderViewSet,
    ItemPackViewSet,
    ItemPackColorViewSet,
    OrderItemViewSet,

)


router = routers.DefaultRouter()

router.register("api/items", ItemViewSet, "items")

router.register("api/users", UserViewSet, "users")

router.register("api/color", ColorViewSet, "color")

router.register("api/packaging", PackagingViewSet, "packaging")

router.register("api/orders", OrderViewSet, "orders")

router.register("api/itempack", ItemPackViewSet, "itempack")

router.register("api/itempackcolor", ItemPackColorViewSet, "itempackcolor")

router.register("api/orderitem", OrderItemViewSet, "orderitem")



urlpatterns = router.urls
