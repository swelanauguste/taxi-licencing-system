from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from . import forms, models


class PlateAssignCreateView(CreateView):
    model = models.Vehicle
    form_class = forms.PlateAssignForm

    def get_initial(self):
        slug = self.kwargs.get("slug")
        vehicle = get_object_or_404(models.Vehicle, slug=slug)
        return {"vehicle": vehicle}

    def get_success_url(self):
        slug = self.kwargs.get("slug")
        vehicle = get_object_or_404(models.Vehicle, slug=slug)
        return reverse("vehicle-detail", kwargs={"slug": vehicle.slug})


class VehicleListView(ListView):
    model = models.Vehicle

    def get_queryset(self):
        query = self.request.GET.get("vehicles", "")
        queryset = models.Vehicle.objects.all().order_by(Lower("chassis_vin"))

        if query:
            return queryset.filter(
                Q(chassis_vin__icontains=query.lower())
                | Q(owner__name__icontains=query.lower())
                | Q(model__name__icontains=query.lower())
                | Q(model__make__name__icontains=query.lower())
                | Q(model__year__icontains=query.lower())
            ).distinct()
        return queryset


class VehicleDetailView(DetailView):
    model = models.Vehicle


class VehicleCreateView(CreateView):
    model = models.Vehicle
    form_class = forms.VehicleForm
    success_url = "/"


class VehicleMakeListView(ListView):
    model = models.VehicleMake


class VehicleMakeDetailView(DetailView):
    model = models.VehicleMake


class VehicleMakeCreateView(CreateView):
    model = models.VehicleMake
    fields = ["name", "description"]
    success_url = "/"


class VehicleModelListView(ListView):
    model = models.VehicleModel


class VehicleModelDetailView(DetailView):
    model = models.VehicleModel


class VehicleModelCreateView(CreateView):
    model = models.VehicleModel
    fields = ["name", "make", "year", "description"]
    success_url = "/"
