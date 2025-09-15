from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # Relation to MenuCategory is possible, e.g. Drinks > Coffee
    menu_category = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def is_main(self):
        return self.menu_category is None

    def is_subcategory(self):
        return self.menu_category is not None

    def __str__(self):
        return (
            f"{self.name} - {self.menu_category.name if self.menu_category else 'Main'}"
        )


class Menu(BaseModel):
    class MenuType(models.IntegerChoices):
        """
        Menu types for restaurant menus on a digital menu board
        """

        MAIN = 1, _("Restaurant menu")
        LUNCH = 2, _("Lunch menu")
        RECOMMENDATIONS = 3, _("Recommendations menu")
    
    name = models.CharField(max_length=255, blank=True, null=True)
    valid_from = models.DateTimeField(blank=False, null=False)
    valid_to = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    menu_type = models.IntegerField(choices=MenuType.choices, default=MenuType.MAIN)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    menu = models.ForeignKey(
        Menu, related_name="products", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.name} - {self.menu.name} ({self.category.name})"
