# Create your views here.
import datetime
from django.db.models.query_utils import Q
from django.http import HttpResponse
from models import *


def sprinklerlog(request):

    zone = request.GET.get('zone')
    direction = request.GET.get('status')

    if direction == 'START':
        new_record = WaterHistory(zone = Zone.objects.get(number=zone), start_date = datetime.datetime.now())
        new_record.save()
    elif direction == 'STOP':
        existing_record = WaterHistory.objects.get(Q(zone= Zone.objects.get(number=zone))&Q(end_date__isnull=True))
        existing_record.end_date = datetime.datetime.now()
        existing_record.save()

    message = 'DONE'
    return HttpResponse(message)
