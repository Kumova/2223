# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Measurement
from .models import Sensor
from serializers import MeasurementSerializer, SensorSerializer


class measurementAPIView(APIView):
    def get(self, request):
        meas=Measurement.objects.all()
#        data = {'name': 'name',
 #                'description': 'description',
 #               'created_at':'created_at'
 #               }
        return Response({MeasurementSerializer(meas, many=True).data})

    def post(self,request):
        serializer=MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        measurement_new=Measurement.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            created_at=request.data['created_at']
        )
        return Response({ MeasurementSerializer(measurement_new).data})

    def patch(self, request):
        serializer=MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        measurement_upd=Measurement.objects.update(
            description=request.data['description'],
            created_at=request.data['created_at']
        )
        return Response({ MeasurementSerializer(measurement_upd).data})


class sensorAPIView(APIView):
    def patch(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sensor_upd = Sensor.objects.update(
            id=request.data['temperature'],
            temperature=request.data['temperature'],
            time_update=request.data['time_update']
        )
        return Response({MeasurementSerializer(sensor_upd).data})










