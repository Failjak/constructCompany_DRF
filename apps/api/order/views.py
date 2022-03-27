from rest_framework.viewsets import ModelViewSet

from apps.models import Order
from .serializers import OrderSerializer


class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
