from rest_framework.viewsets import ModelViewSet

from apps.models import Worker
from .serializers import WorkerSerializer


class WorkerView(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
