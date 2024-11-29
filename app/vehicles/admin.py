from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.VehicleMake)
admin.site.register(models.VehicleModel)
admin.site.register(models.Vehicle)
admin.site.register(models.Plate)