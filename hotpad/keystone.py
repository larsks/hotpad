import os
from keystoneclient.v2_0 import client as ksclient

from .logger import Logger

class Keystone (Logger):
    cfgvars = (
        'auth_url',
        'tenant_id',
        'tenant_name',
        'username',
        'password',
        'region_name',
    )

    def __init__(self, **kwargs):
        super(Keystone, self).__init__()

        self.log.debug('keystone')

        self.credentials = {}
        self._client = None

        for var in self.cfgvars:
            envvar = 'OS_%s' % (var.upper())
            self.credentials[var] = next(
                (v for v in (kwargs.get(var), os.environ.get(envvar))
                if v is not None), None
            )
            self.log.debug('got %s for %s (%s)', self.credentials[var], var, envvar)

        assert self.credentials['auth_url'] is not None
        assert (
            self.credentials['tenant_name'] is not None or
            self.credentials['tenant_id'] is not None)

    @property
    def client(self):
        if self._client is None:
            self._client = ksclient.Client(**self.credentials)

        return self._client

