"""
:author: Gatsby Lee
:since: 2019-08-13

@ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances
"""

import logging
import json

from cloud_compute.gcp import get_compute_engine_service

LOGGER = logging.getLogger(__name__)

# e.g.) zones/us-east1-b/machineTypes/n1-standard-1
TEMPLATE_MACHINE_TYPE = 'zones/{}/machineTypes/{}'


def delete_instance(project, zone, instance_name, service=None):
    _service = service or get_compute_engine_service()
    LOGGER.info('Deleting instance=%s from project=%s, zone=%s',
                instance_name, project, zone)
    return _service.instances().delete(
        project=project, zone=zone, instance=instance_name).execute()


def create_instance(project, zone, instance_name, machine_type, disk_list, service=None):

    _service = service or get_compute_engine_service()

    # Configure the machine
    machine_type = TEMPLATE_MACHINE_TYPE.format(zone, machine_type)

    config = {
        'name': instance_name,
        'machineType': machine_type,
        'disks': disk_list,
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],
        'metadata': {
            'items': [
                {
                    'key': 'user-data',
                    'value': 'hello'
                }
            ]
        }
    }

    LOGGER.info('Creating instance with config=%s', config)
    LOGGER.debug('Creating instance with config:\n%s', json.dumps(config, indent=2))
    opertion_dict = service.instances().insert(
        project=project, zone=zone, body=config).execute()
    return opertion_dict


logging.basicConfig(level=logging.DEBUG)

project = ''
zone = 'us-east1-b'
instance_name = 'test-hello'
machine_type = 'n1-standard-1'


def run_create_instance():

    from cloud_compute.gcp.gcp_osimage import get_centos7_public_image
    source_image = get_centos7_public_image()['selfLink']

    from cloud_compute.gcp.gcp_instance_disk import create_config_bootdisk_from_image
    boot_disk_name = '{}-boot'.format(instance_name)
    boot_disk = create_config_bootdisk_from_image(source_image, boot_disk_name)
    disk_list = [boot_disk]
    operation_dict = create_instance(project, zone, instance_name, machine_type, disk_list)
    print(operation_dict)


def run_check_operation(operation_name, service=None):
    _service = service or get_compute_engine_service()
    response = _service.zoneOperations().get(
        project=project,
        zone=zone,
        operation=operation_name).execute()
    print(response)


# run_create_instance()
# run_check_operation('operation-1565931022636-59034ba58d442-6475c7c6-51e9def7')
delete_instance(project, zone, 'test-hello')
