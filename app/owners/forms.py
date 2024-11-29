from django import forms

from . import models


class OwnerForm(forms.ModelForm):
    class Meta:
        model = models.Owner
        fields = "__all__"
        exclude = ["slug"]
        widgets = {
            "insurance": forms.DateInput(attrs={"type": "date"}),
        }
