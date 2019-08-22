import copy
import collections

from cloud_compute.gcp.gcp_service import *


def get_operation_status(project, zone, operation_name, service=None):
    _service = service or get_compute_engine_service()
    response = _service.zoneOperations().get(
        project=project,
        zone=zone,
        operation=operation_name).execute()
    return response


def get_region_from_zone(zone):
    return zone[:zone.rindex('-')]


class Tags(object):

    __slots__ = ('_tags',)

    def __init__(self, *tags):
        self._tags = set(tags) or set()

    def add(self, tag_name):
        self._tags.add(tag_name)

    def get(self):
        # one level deep copy (shallow copy), to avoid unexpected modification in _tags
        return list(self._tags)

    def remove(self, tag_name):
        self._tags.remove(tag_name)


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


class ServiceAccounts(object):
    __slots__ = ('_accounts', 'MAX_ACCOUNTS')

    MAX_ACCOUNTS = 1

    def __init__(self):
        self._accounts = collections.defaultdict(set)

    def add(self, email, *scopes):
        if email not in self._accounts and len(self._accounts) == self.MAX_ACCOUNTS:
            raise Exception('Only one service account per VM instance is supported')
            # Only one service account per VM instance is supported.
        for s in scopes:
            self._accounts[email].add(s)

    def get(self):
        r = []
        for k in self._accounts:
            r.append({'email': k, 'scopes': list(self._accounts[k])})
        return r

    def remove_email(self, email):
        del self._accounts[email]

    def remove_scope(self, email, scope):
        self._accounts[email].remove(scope)


__all__ = (
    'get_compute_engine_service',
    'get_operation_status',
    'get_region_from_zone',
)
