from rest_framework.viewsets import ModelViewSet

from apps.models import Provider
from .serializers import ProviderSerializer


class ProviderView(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
