"""
:author: Gatsby Lee
:since: 2019-08-13
"""
from cloud_compute.gcp import get_compute_engine_service

# e.g.) zones/us-east1-b/machineTypes/n1-standard-1
TEMPLATE_MACHINE_TYPE = 'zones/{}/machineTypes/{}'

# ref: https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/compute/api/create_instance.py


def create_instance(project, zone, instance_name, machine_type):
    service = get_compute_engine_service()

    # Get the latest Debian Jessie image.
    image_response = service.images().getFromFamily(
        project='debian-cloud', family='debian-9').execute()
    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = TEMPLATE_MACHINE_TYPE.format(zone, machine_type)

    config = {
        'name': instance_name,
        'machineType': machine_type,
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],
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

    opertion_dict = service.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
    return opertion_dict