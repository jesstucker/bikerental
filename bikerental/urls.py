from django.conf.urls import url, include
from django.contrib import admin
from frontend import views as frontend_views

# from api import urls as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', frontend_views.index),
    url(r'^catalog', frontend_views.catalog),
    url(r'^api/', include('api.urls')),

]
