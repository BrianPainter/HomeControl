# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RainBarrel'
        db.create_table('rainbarrel_rainbarrel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('rainbarrel', ['RainBarrel'])

        # Adding model 'WaterLevel'
        db.create_table('rainbarrel_waterlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rainbarrel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rainbarrel.RainBarrel'])),
            ('log_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('measurement', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('rainbarrel', ['WaterLevel'])

    def backwards(self, orm):
        # Deleting model 'RainBarrel'
        db.delete_table('rainbarrel_rainbarrel')

        # Deleting model 'WaterLevel'
        db.delete_table('rainbarrel_waterlevel')

    models = {
        'rainbarrel.rainbarrel': {
            'Meta': {'object_name': 'RainBarrel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'rainbarrel.waterlevel': {
            'Meta': {'object_name': 'WaterLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'measurement': ('django.db.models.fields.IntegerField', [], {}),
            'rainbarrel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rainbarrel.RainBarrel']"})
        }
    }

    complete_apps = ['rainbarrel']