from rest_framework import serializers

from rest_framework_serializer_extensions.serializers import (
    SerializerExtensionsMixin)

from .models import Country, City


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'code', 'url')
        read_only = ('id', 'url')


class CitySerializer(SerializerExtensionsMixin, serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'url')

        read_only = ('id', 'url', 'country', 'country_id_resolved')

        expandable_fields = dict(
            country=dict(
                serializer=CountrySerializer,
                read_only=False,
                # id_source=False
            )
        )
