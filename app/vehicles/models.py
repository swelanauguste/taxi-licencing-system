from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from owners.models import Owner

# Create your models here.


class VehicleMake(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100)
    make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, default=2000)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.make.name} {self.name} {self.year}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make.name}-{self.name}-{self.year}"


class Vehicle(models.Model):
    """
    Vehicle information
    """

    slug = models.SlugField(max_length=100, unique=True, blank=True)
    owner = models.ManyToManyField(Owner, related_name="vehicles")
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    chassis_vin = models.CharField("chassis/vin", max_length=30, unique=True)
    insurance = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.chassis_vin}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.chassis_vin}"


class Plate(models.Model):
    """
    Plate
    """

    plate = models.CharField(max_length=6)
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="plates"
    )

    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.plate}"
