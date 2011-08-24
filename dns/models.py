from django.db import models

class Handle(models.Model):
    def __unicode__(self):
        return 'HANDLE-%d' % self.pk

class HandleData(models.Model):
    handle = models.ForeignKey(Handle)
    field = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        ordering = ['handle', 'field']
        unique_together = ('handle', 'field')

class Domain(models.Model):
    name = models.CharField(max_length=63, primary_key=True)
    ttl = models.PositiveIntegerField(default=14400)

    handles = models.ManyToManyField(Handle, through='DomainHandle')

    @models.permalink
    def get_absolute_url(self):
        return ('domain_detail', [self.pk])

    def __unicode__(self):
        return self.name

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
    name = models.CharField(max_length=63, blank=True)
    type = models.CharField(max_length=5, choices=RR_TYPES)
    ttl = models.PositiveIntegerField(blank=True)
    data = models.CharField(max_length=255)

    def __unicode__(self):
        if self.name:
            return ".".join([self.name, self.domain.name])
        else:
            return self.domain.name

class DomainHandle(models.Model):
    HANDLE_TYPES = (
            ('tech', 'Technical Contact'),
            ('admin', 'Administrative Contact'),
            ('owner', 'Domain Owner'),
    )
    handle = models.ForeignKey(Handle)
    domain = models.ForeignKey(Domain)
    type = models.CharField(max_length=5, choices=HANDLE_TYPES)

    class Meta:
        unique_together = ('domain', 'type')
