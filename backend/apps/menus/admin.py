from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import Category, Menu, Product


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass
