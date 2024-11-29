from django.urls import path

from . import views

urlpatterns = [
    path("", views.OwnerListView.as_view(), name="owner-list"),
    path("create/", views.OwnerCreateView.as_view(), name="owner-create"),
    path("detail/<slug:slug>/", views.OwnerDetailView.as_view(), name="owner-detail"),
]
