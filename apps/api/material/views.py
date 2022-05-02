from rest_framework.viewsets import ModelViewSet

from .serializers import MaterialSerializer
from apps.models import Material


class MaterialView(ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
