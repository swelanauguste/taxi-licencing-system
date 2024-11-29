from django import forms

from . import models

PLATE_CHOICE_LIST = [
    (f"TX{i}", f"TX{i}") for i in range(1, 10000)
]  # Keep the plate format as strings


class PlateAssignForm(forms.ModelForm):
    plate = forms.ChoiceField(
        choices=PLATE_CHOICE_LIST
    )  # Use ChoiceField without coercing to int

    class Meta:
        model = models.Plate
        fields = ["plate", "vehicle"]


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.Vehicle
        fields = "__all__"
        exclude = ["slug"]
        widgets = {
            "insurance": forms.DateInput(attrs={"type": "date"}),
        }
