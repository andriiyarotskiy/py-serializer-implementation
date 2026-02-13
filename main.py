import io

from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_str = json.dumps(serializer.data, separators=(",", ":"))
    return json_str.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car | None:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)

    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return Car.objects.create(**serializer.validated_data)
    return None
