from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from . import forms, models


# Create your views here.
class OwnerListView(ListView):
    model = models.Owner

    def get_queryset(self):
        query = self.request.GET.get("owners", "")
        queryset = models.Owner.objects.all().order_by(Lower("name"))

        if query:
            return queryset.filter(
                Q(name__icontains=query.lower())
                | Q(last_name__icontains=query.lower())
                | Q(email__icontains=query.lower())
                | Q(phone__icontains=query.lower())
                | Q(phone1__icontains=query.lower())
                | Q(address__icontains=query.lower())
                | Q(address1__icontains=query.lower())
            ).distinct()
        return queryset


class OwnerDetailView(DetailView):
    model = models.Owner


class OwnerCreateView(CreateView):
    model = models.Owner
    form_class = forms.OwnerForm
