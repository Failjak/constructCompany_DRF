from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import MaterialSerializer
from apps.models import Material


class MaterialView(RetrieveModelMixin,
                   ListModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
