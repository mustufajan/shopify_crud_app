from django.db import models
from django.db.models import (
    CharField,
    DecimalField,
    ManyToManyField,
    BooleanField,
    IntegerField,
    Model,
)


class InventoryCollection(Model):
    collection_name = CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.id}_{self.collection_name}"


class InventoryItem(Model):
    item_name = CharField(max_length=100, null=False, blank=False)
    item_description = CharField(max_length=10000, null=False, blank=False)
    item_price = DecimalField(decimal_places=2, max_digits=10)
    collection = ManyToManyField(
        InventoryCollection, related_name="inventory_items", blank=True
    )
    item_quantity = IntegerField(default=0, null=False, blank=False)
    archived = BooleanField(default=False)

    def __str__(self):
        return f"{self.id}_{self.item_name}"
