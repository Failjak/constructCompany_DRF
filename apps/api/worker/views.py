from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.models import Worker
from .serializers import WorkerSerializer


class WorkerView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
