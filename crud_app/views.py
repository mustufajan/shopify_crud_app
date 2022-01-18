from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .exceptions import InventoryItemDoesNotExistException
from .models import InventoryCollection, InventoryItem
from .serializers import InventoryItemSerializer, InventoryCollectionSerializer


class StandardPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    page_size_query_description = "The number of results to return per page"
    max_page_size = 50


class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.filter(archived=False).order_by("id")
    serializer_class = InventoryItemSerializer
    pagination_class = StandardPagination

    # overwriting the default destroy view
    def destroy(self, request, pk=None):
        try:
            item_to_be_destroyed = self.queryset.get(id=pk)
        except InventoryItem.DoesNotExist:
            raise InventoryItemDoesNotExistException()

        item_to_be_destroyed.archived = True
        item_to_be_destroyed.save()
        return Response(HTTPStatus.OK)


class InventoryCollectionViewSet(viewsets.ModelViewSet):
    queryset = InventoryCollection.objects.all().order_by("id")
    serializer_class = InventoryCollectionSerializer
    pagination_class = StandardPagination
