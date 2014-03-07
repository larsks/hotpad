from __future__ import absolute_import

import logging

from keystoneclient.v2_0 import client as ksclient
from heatclient import client as heatclient

from .service import Service

class Stack (Service):
    service_type = 'orchestration'
    api_version = '1'

    def __init__(self, stackname, *args, **kwargs):
        self._stack = None
        self._heat = None
        self.name = stackname

        super(Stack, self).__init__(*args, **kwargs)
        
        self.setup_heatclient()
        self.get_stack()

    def setup_heatclient(self):
        self._heat = heatclient.Client(
            self.api_version,
            self.endpoint,
            token=self.auth_token)

    def get_stack(self):
        self._stack = self._heat.stacks.get(self.name)

    @property
    def stack(self):
        return self._stack.to_dict()

    @property
    def outputs(self):
        assert(self._stack is not None)
        return dict((o['output_key'], o['output_value']) 
                    for o in self.stack['outputs'])


