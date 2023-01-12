from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()

    def __str__(self):
        return self.name

class Measurement(models.Model):
    id=models.CharField(primary_key=True, max_length=50)
    temperature=models.CharField(max_length=10)
    time_update=models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.id, self.temperature, self.time_update
