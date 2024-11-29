from django.contrib import admin
from django.urls import include, path
from owners import urls as owner_urls
from vehicles import urls as vehicle_urls

urlpatterns = [
    path("", include(vehicle_urls)),
    path("owners/", include(owner_urls)),
    path("admin/", admin.site.urls),
]
