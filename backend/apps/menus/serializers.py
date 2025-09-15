from django.core.exceptions import ValidationError
from rest_framework import exceptions, serializers

from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["name", "valid_from", "valid_to", "description", "menu_type"]
