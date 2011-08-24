from dns.models import Domain, DnsRecord
from django.contrib import admin

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord

class DomainAdmin(admin.ModelAdmin):
    model = Domain
    inlines = [DnsRecordInline]

admin.site.register(Domain, DomainAdmin)
