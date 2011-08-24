# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HandleData'
        db.create_table('dns_handledata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('handle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dns.Handle'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dns', ['HandleData'])

        # Adding model 'DomainHandle'
        db.create_table('dns_domainhandle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('handle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dns.Handle'])),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dns.Domain'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('dns', ['DomainHandle'])

        # Adding model 'Handle'
        db.create_table('dns_handle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('dns', ['Handle'])


    def backwards(self, orm):
        
        # Deleting model 'HandleData'
        db.delete_table('dns_handledata')

        # Deleting model 'DomainHandle'
        db.delete_table('dns_domainhandle')

        # Deleting model 'Handle'
        db.delete_table('dns_handle')


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
            'handles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dns.Handle']", 'through': "orm['dns.DomainHandle']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63', 'primary_key': 'True'}),
            'ttl': ('django.db.models.fields.PositiveIntegerField', [], {'default': '14400'})
        },
        'dns.domainhandle': {
            'Meta': {'object_name': 'DomainHandle'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dns.Domain']"}),
            'handle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dns.Handle']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'dns.handle': {
            'Meta': {'object_name': 'Handle'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dns.handledata': {
            'Meta': {'ordering': "['handle', 'field']", 'object_name': 'HandleData'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'handle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dns.Handle']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['dns']
