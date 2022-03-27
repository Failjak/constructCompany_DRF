from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth import get_user_model

from .serializers import UserSerializer


User = get_user_model()


class CreateUserView(ViewSet):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserSerializer

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
