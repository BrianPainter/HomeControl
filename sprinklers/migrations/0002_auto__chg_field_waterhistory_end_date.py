# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WaterHistory.end_date'
        db.alter_column('sprinklers_waterhistory', 'end_date', self.gf('django.db.models.fields.DateTimeField')(null=True))
    def backwards(self, orm):

        # Changing field 'WaterHistory.end_date'
        db.alter_column('sprinklers_waterhistory', 'end_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 8, 0, 0)))
    models = {
        'sprinklers.waterhistory': {
            'Meta': {'object_name': 'WaterHistory'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sprinklers.Zone']"})
        },
        'sprinklers.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        'sprinklers.zoneschedule': {
            'Meta': {'object_name': 'ZoneSchedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'run_start_time': ('django.db.models.fields.TimeField', [], {}),
            'run_stop_time': ('django.db.models.fields.TimeField', [], {}),
            'run_weekday': ('django.db.models.fields.IntegerField', [], {}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sprinklers.Zone']"})
        }
    }

    complete_apps = ['sprinklers']