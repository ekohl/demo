from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from dns.models import Domain

urlpatterns = patterns('dns.views',
    url(r'^domain/$', ListView.as_view(
            model=Domain,
            context_object_name="domain_list",
        ),
        name='domain_list'
    ),
    url(r'^domain/(?P<pk>(\w+\.)+\w+)$', DetailView.as_view(
            model=Domain,
            context_object_name="domain",
        ),
        name='domain_detail'
    ),

    url(r'^bind/named.zones.conf$', ListView.as_view(
            model=Domain,
            context_object_name="domain_list",
            template_name="dns/bind/named.zones.conf",
        ),
        name='bind_named.zones.conf'
    ),
    url(r'^bind/(?P<pk>(\w+\.)+\w+).zone$', DetailView.as_view(
            model=Domain,
            context_object_name="domain",
            template_name="dns/bind/template.zone",
        ),
        name='bind_domain.zone'
    ),
)
