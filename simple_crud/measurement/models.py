from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=149,verbose_name="Датчик")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    temperature = models.FloatField(verbose_name="Температура")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата измерения")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        ordering = ['-update_date']
