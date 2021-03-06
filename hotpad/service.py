from __future__ import absolute_import

from .logger import Logger
from .keystone import Keystone

class Service (Logger):
    service_type = None
    endpoint_type = 'publicURL'

    def __init__(self, ksclient=None):
        super(Service, self).__init__()

        if ksclient is None:
            ksclient = Keystone()

        self._ks = ksclient.client
        self.find_endpoint()

    def find_endpoint(self):
        self.endpoint = self._ks.service_catalog.url_for(
            service_type=self.service_type,
            endpoint_type=self.endpoint_type)

    @property
    def auth_token(self):
        return self._ks.auth_token


