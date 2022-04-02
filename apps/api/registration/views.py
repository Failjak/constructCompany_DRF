from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


User = get_user_model()


class CreateUserView(GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny(), ]
        return [permissions.IsAdminUser(), ]

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "User has been created successfully!",
                "user": serializer.data,
            },
            status=status.HTTP_201_CREATED
        )
