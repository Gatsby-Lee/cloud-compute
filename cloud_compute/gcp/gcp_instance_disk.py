"""
:author: Gatsby Lee
:since: 2019-08-15

@ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
"""
from enum import Enum

FORMAT_DISKTYPE = '/projects/%(project)s/zones/%(zone)s/diskTypes/%(diskType)s'


class DiskLifeType(Enum):
    PERSISTENT = 'PERSISTENT'  # default
    SCRATCH = 'SCRATCH'  # tied to instance's lifecycle


class DiskMode(Enum):
    READ_WRITE = 'READ_WRITE'  # default
    READ_ONLY = 'READ_ONLY'


class DiskInerface(Enum):
    # persistent disk must use SCSI only.
    # Local SSD can use either SCSI or NVME.
    SCSI = 'SCSI'
    NVME = 'NVME'


class DiskType(Enum):
    PD_STANDARD = 'pd-standard'
    PD_SSD = 'pd-ssd'
    # Local SSDs cannot be used as boot devices
    LOCAL_SSD = 'local-ssd'


def create_config_persistent_bootdisk_from_image(
    project,
    zone,
    sourceImage,
    diskName,
    diskSizeGb=10,
    autoDelete=True,
    diskType=DiskType.PD_STANDARD
):
    """
    create config for persistent bootdisk from image
    """
    assert type(project) is str
    assert type(zone) is str
    assert type(sourceImage) is str
    assert type(diskName) is str
    assert type(diskSizeGb) is int
    assert type(autoDelete) is bool
    assert type(diskType) is DiskType

    _diskType = FORMAT_DISKTYPE % {
        'project': project,
        'zone': zone,
        'diskType': diskType.value
    }

    config = {
        'boot': True,
        'autoDelete': autoDelete,
        'initializeParams': {
            'diskName': diskName,
            'diskSizeGb': diskSizeGb,
            'diskType': _diskType,
            'sourceImage': sourceImage,
        }
    }
    return config


def create_config_persistent_disk(
    project,
    zone,
    diskName,
    diskSizeGb,
    autoDelete=True,
    diskType=DiskType.PD_STANDARD
):
    """
    create config for persistent disk
    """
    assert type(project) is str
    assert type(zone) is str
    assert type(diskName) is str
    assert type(diskSizeGb) is int
    assert type(autoDelete) is bool
    assert type(diskType) is DiskType

    _diskType = FORMAT_DISKTYPE % {
        'project': project,
        'zone': zone,
        'diskType': diskType.value
    }

    config = {
        'boot': False,
        'autoDelete': autoDelete,
        'initializeParams': {
            'diskName': diskName,
            'diskSizeGb': diskSizeGb,
            'diskType': _diskType,
        }
    }
    return config


__all__ = (
    'DiskLifeType',
    'DiskMode',
    'DiskInerface',
    'DiskType',
    'create_config_persistent_bootdisk_from_image',
    'create_config_persistent_disk',
)
