from rest_framework import viewsets

from tables.models import Table, Leg, Foot
from tables.serializers import TableSerializer, LegSerializer, FootSerializer


class TablesReadOnlyViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    http_method_names = ['get']


class LegsReadOnlyViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer
    http_method_names = ['get']


class FeetReadOnlyViewSet(viewsets.ModelViewSet):
    queryset = Foot.objects.all()
    serializer_class = FootSerializer
    http_method_names = ['get']
