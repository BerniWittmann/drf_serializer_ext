from rest_framework import viewsets, mixins, permissions, status
from rest_framework_serializer_extensions.views import (
    SerializerExtensionsAPIViewMixin)

from .models import City, Country
from .serializers import CountrySerializer, CitySerializer


class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(SerializerExtensionsAPIViewMixin, viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
