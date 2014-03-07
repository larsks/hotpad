import logging

class Logger (object):
    def __init__ (self):
        self.log = logging.getLogger('{}.{}'.format(
            self.__module__, self.__class__.__name__))

