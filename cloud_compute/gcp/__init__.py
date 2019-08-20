from cloud_compute.gcp.gcp_service import *


def get_operation_status(project, zone, operation_name, service=None):
    _service = service or get_compute_engine_service()
    response = _service.zoneOperations().get(
        project=project,
        zone=zone,
        operation=operation_name).execute()
    return response


__all__ = (
    'get_compute_engine_service',
    'get_operation_status',
)
