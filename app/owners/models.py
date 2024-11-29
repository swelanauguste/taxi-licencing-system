# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Owner(models.Model):
    """
    Owner's information

    """

    slug = models.SlugField(max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15)
    phone1 = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    is_private = models.BooleanField(default=False)

    class Meta:
        unique_together = ("name", "last_name")

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name} {self.last_name}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("owner-detail", kwargs={"slug": self.slug})

    def get_name(self):
        if self.name and self.last_name:
            return f"{self.name} {self.last_name}"
        return f"{self.name}"

    def __str__(self):
        if self.name and self.last_name:
            return f"{self.name} {self.last_name}"
        return f"{self.name}"
