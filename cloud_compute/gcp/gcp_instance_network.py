"""
:author: Gatsby Lee
:since: 2019-08-20

@ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
"""
from enum import Enum

DEFAULT_NETWORK = 'global/networks/default'
FORMAT_NETWORK = 'projects/{}/global/networks/{}'
FORMAT_SUBNETWORK = 'regions/{}/subnetworks/{}'

DEFAULT_NETWORK_ACCESS_NAME = 'External NAT'


class NetworkAccessType(Enum):
    ONE_TO_ONE_NAT = 'ONE_TO_ONE_NAT'  # default


def create_default_external_accessible_network():

    config = {
        'network': DEFAULT_NETWORK,
        'accessConfigs': [
            {
                'type': NetworkAccessType.ONE_TO_ONE_NAT.value,
                'name': DEFAULT_NETWORK_ACCESS_NAME
            }
        ]
    }
    return config


def create_external_accessible_network(project, region, network, subnetwork,
                                       networkIP=None, natIP=None):

    _network = FORMAT_NETWORK.format(project, network)
    _subnetwork = FORMAT_SUBNETWORK.format(region, subnetwork)
    _accessConfigs = []
    config = {
        'network': _network,
        'subnetwork': _subnetwork,
        'accessConfigs': _accessConfigs
    }

    _accessConfig = {
        'type': NetworkAccessType.ONE_TO_ONE_NAT.value,
        'name': DEFAULT_NETWORK_ACCESS_NAME
    }
    if natIP is not None:
        _accessConfig['natIP'] = natIP
    _accessConfigs.append(_accessConfig)

    if networkIP is not None:
        config['networkIP'] = networkIP

    return config


__all__ = (
    'create_external_accessible_network',
)
