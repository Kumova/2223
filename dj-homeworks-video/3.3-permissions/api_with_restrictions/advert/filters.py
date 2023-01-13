from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from advert.models import Advert


class AdvertFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status', 'created_at']

    class Meta:
        model = Advert
