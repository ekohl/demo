# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Domain'
        db.create_table('dns_domain', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63, primary_key=True)),
            ('ttl', self.gf('django.db.models.fields.PositiveIntegerField')(default=14400)),
        ))
        db.send_create_signal('dns', ['Domain'])

        # Adding model 'DnsRecord'
        db.create_table('dns_dnsrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dns.Domain'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('ttl', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('data', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dns', ['DnsRecord'])


    def backwards(self, orm):
        
        # Deleting model 'Domain'
        db.delete_table('dns_domain')

        # Deleting model 'DnsRecord'
        db.delete_table('dns_dnsrecord')


    models = {
        'dns.dnsrecord': {
            'Meta': {'object_name': 'DnsRecord'},
            'data': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dns.Domain']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'ttl': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'dns.domain': {
            'Meta': {'object_name': 'Domain'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'primary_key': 'True'}),
            'ttl': ('django.db.models.fields.PositiveIntegerField', [], {'default': '14400'})
        }
    }

    complete_apps = ['dns']
