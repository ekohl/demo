from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=63, primary_key=True)
    ttl = models.PositiveIntegerField(default=14400)

class DnsRecord(models.Model):
    RR_TYPES = (
            ('A', 'Host Address'),
            ('NS', 'Name Server'),
            ('CNAME', 'Canonical Name'),
            ('PTR', 'Domain Name Pointer'),
            ('MX', 'Mail Exchange'),
            ('TXT', 'Text'),
            ('SRV', 'Service'),
    )

    domain = models.ForeignKey(Domain)
    name = models.CharField(max_length=63)
    type = models.CharField(max_length=5, choices=RR_TYPES)
    ttl = models.PositiveIntegerField(blank=True)
    data = models.CharField(max_length=255)
