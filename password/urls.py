from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PasswordViewSet

router_v1 = DefaultRouter()
router_v1.register(r"password", PasswordViewSet, basename="password")

urlpatterns = [
    path("", include(router_v1.urls)),
    path(
        "password/<str:service_name>/",
        PasswordViewSet.as_view({"post": "create", "get": "retrieve"}),
    ),
]
