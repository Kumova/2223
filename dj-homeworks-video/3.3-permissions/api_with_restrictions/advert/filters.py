from datetime import timezone
from django_filters import rest_framework as filters, IsoDateTimeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from advert.models import Advert


class AdvertFilter(filters.FilterSet):
    status = filters.CharFilter()
    created_at=IsoDateTimeFilter()
 #   created_at=filters.DateTimeFilter(field_name="created_at",datetime= timezone.now())

    class Meta:
        model = Advert,
        fields = ['status', 'created_at']







