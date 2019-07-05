from django.db import IntegrityError, transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import Shoe
from .serializers import ShoeSerializer, ShoeCsvSerializer


class ShoeViewSet(ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('sku', 'name', 'color', 'stock', 'price')
    search_fields = ('name', 'color',)

    def get_serializer_class(self):
        if 'csv_import' in self.request.path:
            return ShoeCsvSerializer
        return ShoeSerializer

    @action(methods=['post'], detail=False, url_path='csv_import', url_name='csv-import')
    @transaction.atomic
    def import_csv(self, request):
        pass
