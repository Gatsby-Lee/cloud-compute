"""
:author: Gatsby Lee
:since: 2019-08-15

@ref:
    https://cloud.google.com/compute/docs/images
    https://cloud.google.com/container-optimized-os/docs/release-notes
"""
from cloud_compute.gcp import get_compute_engine_service


SHIELDED_IMAGE_PROJECT = 'gce-uefi-images'


def _get_image(project, family, service=None):
    _service = service or get_compute_engine_service()
    return _service.images().getFromFamily(
        project=project, family=family).execute()


def get_centos7_public_image_with_shield(service=None):
    return _get_image(SHIELDED_IMAGE_PROJECT, 'centos-7', service=service)


def get_centos6_public_image_with_shield(service=None):
    return _get_image(SHIELDED_IMAGE_PROJECT, 'centos-6', service=service)


def get_centos7_public_image(service=None):
    return _get_image('centos-cloud', 'centos-7', service=service)


def get_centos6_public_image(service=None):
    return _get_image('centos-cloud', 'centos-6', service=service)


def get_debian9_public_image(service=None):
    return _get_image('debian-cloud', 'debian-9', service=service)


def get_google_cos_image_with_shield(service=None):
    return _get_image(SHIELDED_IMAGE_PROJECT, 'cos-stable', service=service)


def get_google_cos_image(service=None):
    return _get_image('cos-cloud', 'cos-stable', service=service)


__all__ = (
    'get_centos7_public_image',
    'get_centos6_public_image',
    'get_centos7_public_image_with_shield',
    'get_centos6_public_image_with_shield',
    'get_debian9_public_image',
    'get_google_cos_image_with_shield',
    'get_google_cos_image',
)
