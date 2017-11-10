from django.conf.urls import url, include
from api.serializers import router

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]