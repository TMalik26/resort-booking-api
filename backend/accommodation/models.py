from autoslug import AutoSlugField
from django.db import models
from slugify import slugify


def custom_slugify(value):
    return slugify(value, lowercase=True)


class Property(models.Model):
    name = models.CharField(max_length=255)

    slug = AutoSlugField(
        populate_from="name", unique=True, always_update=True, slugify=custom_slugify
    )

    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="images"
    )
    image = models.CharField(max_length=1000, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return f"Image for {self.property.name}"
