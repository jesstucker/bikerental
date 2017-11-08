from django.conf.urls import url, include
from api.serializers import router, BikeDatesReportView

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'test/', BikeDatesReportView.as_view()),
]