from dns.models import Domain, DomainHandle, DnsRecord, Handle, HandleData
from django.contrib import admin

class DnsRecordInline(admin.TabularInline):
    model = DnsRecord

class DomainHandleInline(admin.TabularInline):
    model = DomainHandle

class DomainAdmin(admin.ModelAdmin):
    model = Domain
    inlines = [DomainHandleInline, DnsRecordInline]

admin.site.register(Domain, DomainAdmin)

class HandleDataInline(admin.TabularInline):
    model = HandleData

class HandleAdmin(admin.ModelAdmin):
    model = Handle
    inlines = [HandleDataInline]

admin.site.register(Handle, HandleAdmin)
