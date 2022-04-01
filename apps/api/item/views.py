from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import ItemSerializer
from apps.models import Item


class ItemView(RetrieveModelMixin,
               ListModelMixin,
               DestroyModelMixin,
               GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

