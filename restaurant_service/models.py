from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import DecimalField, CharField

from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    years_of_experience = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant_service:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=255, default="Unknown")
    description = models.TextField(
        max_length=1000,
        help_text="Select a description for this dish..."
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)  # Добавлено значение по умолчанию
    dish_type = models.ForeignKey('restaurant_service.DishType', on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name
