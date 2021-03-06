from rest_framework import serializers

from tables.models import Table, Leg, Foot


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('__all__')


class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leg
        fields = '__all__'


class FootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foot
        fields = '__all__'
