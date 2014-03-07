import os
from keystoneclient.v2_0 import client as ksclient

class Keystone (object):
    cfgvars = (
        'auth_url',
        'tenant_id',
        'tenant_name',
        'username',
        'password',
    )

    def __init__(self, **kwargs):

        self.credentials = {}
        self._client = None

        for var in self.cfgvars:
            envvar = 'OS_%s' % (var.upper())
            self.credentials[var] = (
                kwargs.get(var, os.environ.get(envvar)))

        assert self.credentials['auth_url'] is not None
        assert (
            self.credentials['tenant_name'] is not None or
            self.credentials['tenant_id'] is not None)

    @property
    def client(self):
        if self._client is None:
            self._client = ksclient.Client(**self.credentials)

        return self._client

