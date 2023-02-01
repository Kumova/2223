from urllib import request


from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet
from .models import Advert
from .serializers import AdvertSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdvertViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at']
    throttle_classes = [AnonRateThrottle]



    def get_permissions(self):

        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []





#        if self.action == 'list':
#            permission_classes = [IsAuthenticated]
 #       else:
 #           permission_classes = [IsAdminUser]
#        return [permission() for permission in permission_classes]


