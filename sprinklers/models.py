from django.db import models

# Create your models here.

class Zone(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)

class ZoneSchedule(models.Model):
    zone = models.ForeignKey(Zone)
    run_start_time = models.TimeField()
    run_stop_time = models.TimeField()
    run_weekday = models.IntegerField()

class WaterHistory(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    zone = models.ForeignKey(Zone)

