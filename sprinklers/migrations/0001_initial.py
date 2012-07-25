# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zone'
        db.create_table('sprinklers_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('sprinklers', ['Zone'])

        # Adding model 'ZoneSchedule'
        db.create_table('sprinklers_zoneschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinklers.Zone'])),
            ('run_start_time', self.gf('django.db.models.fields.TimeField')()),
            ('run_stop_time', self.gf('django.db.models.fields.TimeField')()),
            ('run_weekday', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('sprinklers', ['ZoneSchedule'])

        # Adding model 'WaterHistory'
        db.create_table('sprinklers_waterhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sprinklers.Zone'])),
        ))
        db.send_create_signal('sprinklers', ['WaterHistory'])

    def backwards(self, orm):
        # Deleting model 'Zone'
        db.delete_table('sprinklers_zone')

        # Deleting model 'ZoneSchedule'
        db.delete_table('sprinklers_zoneschedule')

        # Deleting model 'WaterHistory'
        db.delete_table('sprinklers_waterhistory')

    models = {
        'sprinklers.waterhistory': {
            'Meta': {'object_name': 'WaterHistory'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
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