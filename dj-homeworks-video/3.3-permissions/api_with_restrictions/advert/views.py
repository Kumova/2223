
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advert
from .serializers import AdvertSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdvertViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at']



    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
