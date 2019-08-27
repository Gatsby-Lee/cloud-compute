"""
:author: Gatsby Lee
:since: 2019-08-25
"""


class Metadatas(object):
    __slots__ = ('_metadatas',)

    def __init__(self, **kwargs):
        self._metadatas = {}
        if kwargs:
            for k in kwargs:
                self._metadatas[k] = kwargs[k]

    def add(self, key, value):
        self._metadatas[key] = value

    def get(self):
        r = []
        for k in self._metadatas:
            r.append({'key': k, 'value': self._metadatas[k]})
        return r

    def remove(self, key):
        del self._metadatas[key]

    def enable_oslogin(self):
        self.add('enable-oslogin', 'TRUE')

    def disable_oslogin(self):
        self.add('enable-oslogin', 'FALSE')
