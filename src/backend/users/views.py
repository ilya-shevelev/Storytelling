from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsAccountOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAccountOwnerOrReadOnly,)

    def get_serializer_class(self):
        if self.action == "retrieve" or "update":
            return UserSerializer
