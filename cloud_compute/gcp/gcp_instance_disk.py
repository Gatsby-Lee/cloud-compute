"""
:author: Gatsby Lee
:since: 2019-08-15

@ref: https://cloud.google.com/compute/docs/reference/rest/v1/instances/insert
"""
from enum import Enum


class DiskType(Enum):
    PERSISTENT = 'PERSISTENT'  # default
    SCRATCH = 'SCRATCH'


class DiskMode(Enum):
    READ_WRITE = 'READ_WRITE'  # default
    READ_ONLY = 'READ_ONLY'


class DiskInerface(Enum):
    # persistent disk must use SCSI only.
    # Local SSD can use either SCSI or NVME.
    SCSI = 'SCSI'
    NVME = 'NVME'


def create_config_bootdisk_from_image(
    sourceImage,
    diskName,
    diskSizeGb=10,
    autoDelete=True,
    # using Enum
    diskType=DiskType.PERSISTENT,
    diskMode=DiskMode.READ_WRITE,
    diskInterface=DiskInerface.SCSI,
):
    """
    create config for bootdisk from image
    """
    assert type(sourceImage) is str
    assert type(diskName) is str
    assert type(diskSizeGb) is int
    assert type(autoDelete) is bool
    assert type(diskType) is DiskType
    assert type(diskMode) is DiskMode
    assert type(diskInterface) is DiskInerface

    config = {
        'boot': True,
        'autoDelete': autoDelete,
        'diskType': diskType.value,
        'mode': diskMode.value,
        'interface': diskInterface.value,
        'initializeParams': {
            'sourceImage': sourceImage,
            'diskName': diskName,
            'diskSizeGb': diskSizeGb
        }
    }

    return config


__all__ = (
    'DiskType',
    'DiskMode',
    'DiskInerface',
    'create_config_bootdisk_from_image',
)
