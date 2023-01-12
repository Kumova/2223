from rest_framework import serializers
from .models import Measurement
from .models import Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    temperature = serializers.CharField(max_length=10)
    time_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']