"""
:author: Gatsby Lee
:author: 2019-08-24

ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
"""

# e.g.) zones/us-east1-b/machineTypes/n1-standard-1
TEMPLATE_MACHINE_TYPE = 'zones/{}/machineTypes/{}'


def get_machine_type_fullname(zone, machine_type):
    machine_type = machine_type.strip()
    if machine_type.startswith('custom-'):
        _, memory = machine_type[machine_type.index('-') + 1:].split('-')
        if int(memory) % 256:
            raise ValueError('Memory must be a multiple of 256 MB')

    return TEMPLATE_MACHINE_TYPE.format(zone, machine_type)
