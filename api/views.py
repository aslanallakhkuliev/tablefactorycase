from rest_framework import viewsets, permissions

from tables.models import Table, Leg, Foot
from tables.serializers import TableSerializer, LegSerializer, FootSerializer


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAuthenticated]


class LegViewSet(viewsets.ModelViewSet):
    queryset = Leg.objects.all()
    serializer_class = LegSerializer
    permission_classes = [permissions.IsAuthenticated]


class FootViewSet(viewsets.ModelViewSet):
    queryset = Foot.objects.all()
    serializer_class = FootSerializer
    permission_classes = [permissions.IsAuthenticated]
