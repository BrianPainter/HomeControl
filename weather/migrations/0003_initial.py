# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('weather_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sysname', self.gf('django.db.models.fields.SlugField')(default='', unique=True, max_length=200, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('weather', ['Location'])

        # Adding model 'WeatherLog'
        db.create_table('weather_weatherlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weather.Location'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('temperature', self.gf('django.db.models.fields.IntegerField')()),
            ('humidity', self.gf('django.db.models.fields.IntegerField')()),
            ('wind_speed', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('visibility', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('weather', ['WeatherLog'])

    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('weather_location')

        # Deleting model 'WeatherLog'
        db.delete_table('weather_weatherlog')

    models = {
        'weather.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sysname': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'weather.weatherlog': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'WeatherLog'},
            'humidity': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weather.Location']"}),
            'temperature': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'visibility': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'wind_speed': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['weather']