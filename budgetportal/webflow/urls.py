from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    "infrastructure-projects/provincial/search",
    views.ProvInfraProjectSearchView,
    basename="provincial-infrastructure-project-api",
)

urlpatterns = [
    url(
        r"^infrastructure-projects/provincial/$",
        views.provincial_infrastructure_project_list,
        name="provincial-infra-project-list",
    ),
    url(
        r"^infrastructure-projects/provincial/(?P<id>\d+)-(?P<slug>[\w-]+)$",
        views.provincial_infrastructure_project_detail,
        name="provincial-infra-project-detail",
    ),
    url(r"^api/v1/", include(router.urls)),
]
