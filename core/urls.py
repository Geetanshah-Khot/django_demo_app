from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, joke_api, report_view

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("joke/", joke_api),
    path("report/", report_view),
]
