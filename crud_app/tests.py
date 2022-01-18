import json
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from .models import InventoryCollection, InventoryItem


class InventoryItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            InventoryItem.objects.create(
                item_name=f"Test_{i}",
                item_description="Test Description",
                item_price=i,
                item_quantity=10,
            )
        InventoryCollection.objects.create(
            collection_name="Test Collection",
        )

    def test_list_inventory_item(self):
        """
        Testing the list endpoint
        """
        c = self.client
        page_size = 3
        url = reverse("inventory_item-list")
        url += f"?page_size={page_size}"
        response = c.get(url)

        # checking pagination
        self.assertEqual(len(response.data["results"]), page_size)
        self.assertEqual(response.data["count"], 10)

    def test_delete_inventory_item(self):
        """
        Testing the delete endpoint
        """
        c = self.client
        id_to_delete = InventoryItem.objects.first().id
        url = reverse("inventory_item-detail", kwargs={"pk": id_to_delete})
        response = c.delete(url)
        # checking endpoint's response
        self.assertEquals(response.status_code, HTTPStatus.OK)
        # checking against db
        self.assertEquals(InventoryItem.objects.get(id=id_to_delete).archived, True)

    def test_delete_non_existinginventory_item(self):
        """
        Test deleting a non-existing item
        """
        id_to_delete = InventoryItem.objects.last().id + 1
        c = self.client
        url = reverse("inventory_item-detail", kwargs={"pk": id_to_delete})
        response = c.delete(url)
        self.assertEquals(response.status_code, HTTPStatus.NOT_FOUND)

    def test_retrieve_inventory_item(self):
        """
        Testing retrieving an inventory item
        """
        c = self.client
        pk = InventoryItem.objects.first().id
        url = reverse("inventory_item-detail", kwargs={"pk": pk})
        response = c.get(url)
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_patch_inventory_item(self):
        """
        Testing the editing an inventory item
        """
        c = self.client
        pk = InventoryItem.objects.first().id
        url = reverse("inventory_item-detail", kwargs={"pk": pk})
        collection_id = InventoryCollection.objects.first().id

        # assign to collection
        body = {"collection": [collection_id]}
        response = c.patch(url, data=json.dumps(body), content_type="application/json")
        self.assertEquals(response.status_code, HTTPStatus.OK)

        # remove from collection
        body = {"collection": []}
        response = c.patch(url, data=json.dumps(body), content_type="application/json")
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_create_inventory_item(self):
        """
        Testing the creating an inventory item
        """
        c = self.client
        url = reverse("inventory_item-list")
        collection_id = InventoryCollection.objects.first().id

        body = {
            "item_name": "Test_Create",
            "item_description": "Test Description",
            "item_price": 3,
            "item_quantity": 100,
            "collection": [collection_id],
        }
        response = c.post(url, data=json.dumps(body), content_type="application/json")
        self.assertEquals(response.status_code, HTTPStatus.CREATED)
