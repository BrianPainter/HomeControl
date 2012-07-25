__author__ = 'painter'

from djangorestframework.resources import ModelResource
from rainbarrel.models import RainBarrelWaterLevel


class WaterLevelResource(ModelResource):
    model = RainBarrelWaterLevel