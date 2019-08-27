"""
:author: Gatsby Lee
:since: 2019-08-26
"""
import logging

from cloud_compute.gcp import get_dataproc_service


LOGGER = logging.getLogger(__name__)


def create_dataproc_cluster(project, region, cluster_config, service=None):

    _service = service or get_dataproc_service()

    LOGGER.info('Creating Dataproc cluster on project=%s, region=%s',
                project, region)
    opertion_dict = _service.projects().regions().clusters().create(
        projectId=project, region=region, body=cluster_config).execute()
    return opertion_dict
