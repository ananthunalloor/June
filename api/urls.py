from django.conf.urls import url, include
from rest_framework import routers
from api.views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'v1/', include(router.urls)),
]