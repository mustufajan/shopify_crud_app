from django.contrib import admin
from .models import InventoryItem, InventoryCollection

admin.site.register(InventoryItem)
admin.site.register(InventoryCollection)
