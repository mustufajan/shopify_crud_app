from rest_framework.exceptions import APIException


class InventoryItemDoesNotExist(APIException):
    status_code = 404
    default_detail = "The inventory item does not exist."
    default_code = "inventory_item_does_not_exist"
    pointer = "inventory.item"
