from django.urls import path

from . import views

urlpatterns = [
    path("", views.VehicleListView.as_view(), name="vehicle-list"),
    path("create/", views.VehicleCreateView.as_view(), name="vehicle-create"),
    path(
        "create-make/",
        views.VehicleMakeCreateView.as_view(),
        name="vehicle-make-create",
    ),
    path(
        "create-model/",
        views.VehicleModelCreateView.as_view(),
        name="vehicle-model-create",
    ),
    path(
        "vehicle/<slug:slug>/assign-plate/",
        views.PlateAssignCreateView.as_view(),
        name="vehicle-plate-create",
    ),
    path(
        "detail/<slug:slug>/", views.VehicleDetailView.as_view(), name="vehicle-detail"
    ),
]
