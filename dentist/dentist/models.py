from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class SlugNameModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class OurTeam(SlugNameModel):
    img = models.ImageField(blank=True)
    description = models.TextField(
        max_length=1000,
        blank=True
    )


class Service(SlugNameModel):
    img = models.ImageField(blank=True)
    description = models.TextField(
        max_length=1000,
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse('dentist:service_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
