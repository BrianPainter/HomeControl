# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'WaterLevel'
        db.delete_table('rainbarrel_waterlevel')

        # Adding model 'RainBarrelWaterLevel'
        db.create_table('rainbarrel_rainbarrelwaterlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rainbarrel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rainbarrel.RainBarrel'])),
            ('log_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('measurement', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('rainbarrel', ['RainBarrelWaterLevel'])

    def backwards(self, orm):
        # Adding model 'WaterLevel'
        db.create_table('rainbarrel_waterlevel', (
            ('rainbarrel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rainbarrel.RainBarrel'])),
            ('log_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('measurement', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('rainbarrel', ['WaterLevel'])

        # Deleting model 'RainBarrelWaterLevel'
        db.delete_table('rainbarrel_rainbarrelwaterlevel')

    models = {
        'rainbarrel.rainbarrel': {
            'Meta': {'object_name': 'RainBarrel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'rainbarrel.rainbarrelwaterlevel': {
            'Meta': {'object_name': 'RainBarrelWaterLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'measurement': ('django.db.models.fields.IntegerField', [], {}),
            'rainbarrel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rainbarrel.RainBarrel']"})
        }
    }

    complete_apps = ['rainbarrel']