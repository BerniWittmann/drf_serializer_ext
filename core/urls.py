from django.urls import path, include

from rest_framework import routers

from .views import CityViewSet, CountryViewSet


router = routers.DefaultRouter()


router.register(r'cities', CityViewSet, base_name='city')
router.register(r'countries', CountryViewSet, base_name='country')


urlpatterns = [
    path('api/', include(router.urls)),
]
