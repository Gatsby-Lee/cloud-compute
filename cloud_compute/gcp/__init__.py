import copy
import collections

from cloud_compute.gcp.gcp_service import (
    get_compute_engine_service,
    get_dataproc_service,
)
from cloud_compute.gcp.gcp_service_account import ServiceAccounts
from cloud_compute.gcp.gcp_metadata import Metadatas


def get_operation_status(project, zone, operation_name, service=None):
    _service = service or get_compute_engine_service()
    response = _service.zoneOperations().get(
        project=project, zone=zone, operation=operation_name).execute()
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
        # one level deep copy (shallow copy), to avoid unexpected modification
        return list(self._tags)

    def remove(self, tag_name):
        self._tags.remove(tag_name)


class Labels(object):

    __slots__ = ('_labels',)

    def __init__(self, **labels):
        self._labels = labels or dict()

    def add(self, label_key, label_value):
        self._labels[label_key] = label_value

    def get(self):
        # one level deep copy (shallow copy), to avoid unexpected modification
        return dict(self._labels)

    def remove(self, label_key):
        del self._labels[label_key]


__all__ = (
    'get_compute_engine_service',
    'get_dataproc_service',
    'get_operation_status',
    'get_region_from_zone',
    'Labels',
    'Metadatas',
    'ServiceAccounts',
    'Tags',
)
