from django.db import models

# Create your models here.

class RainBarrel(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class RainBarrelWaterLevel(models.Model):
    rainbarrel = models.ForeignKey(RainBarrel)
    log_date = models.DateField(auto_now_add=True)
    measurement = models.IntegerField()

    def __unicode__(self):
        return self.rainbarrel.name


