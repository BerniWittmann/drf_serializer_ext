from rest_framework import serializers

from rest_framework_serializer_extensions.serializers import (
    SerializerExtensionsMixin)

from .models import Country, City


class CountrySerializer(SerializerExtensionsMixin, serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'code', 'url')
        read_only = ('id', 'url')


class CitySerializer(SerializerExtensionsMixin, serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'url')

        read_only = ('id', 'url',)

        expandable_fields = dict(
            country=dict(
                serializer=CountrySerializer,
                read_only=False,
            )
        )

    def create(self, validated_data):
        validated_data.pop('country_id_resolved')
        return super().create(validated_data)
