"""
:author: Gatsby Lee
:since: 2019-08-13

@ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances
"""

import logging

from cloud_compute.gcp import (
    get_compute_engine_service,
)


LOGGER = logging.getLogger(__name__)


def create_instance(project, zone, instance_config, service=None):

    _service = service or get_compute_engine_service()

    LOGGER.info('Creating instance on project=%s, zone=%s',
                project, zone)
    opertion_dict = _service.instances().insert(
        project=project, zone=zone, body=instance_config).execute()
    return opertion_dict


def delete_instance(project, zone, instance_name, service=None):

    _service = service or get_compute_engine_service()

    LOGGER.info('Deleting instance=%s from project=%s, zone=%s',
                instance_name, project, zone)
    return _service.instances().delete(
        project=project, zone=zone, instance=instance_name).execute()
