import pytest

from cloud_compute.gcp.gcp_instance_disk import *


def test_create_config_bootdisk_from_image_with_default_value():

    sourceImage = 'myimage'
    diskName = 'mydisk'
    ret_config = create_config_bootdisk_from_image(
        sourceImage, diskName
    )

    expected_config = {
        'boot': True,
        'autoDelete': True,
        'diskType': DiskType.PERSISTENT.value,
        'mode': DiskMode.READ_WRITE.value,
        'interface': DiskInerface.SCSI.value,
        'initializeParams': {
            'sourceImage': sourceImage,
            'diskName': diskName,
            'diskSizeGb': 10,
        }
    }

    assert ret_config == expected_config


def test_create_config_bootdisk_from_image_with_arguments():

    sourceImage = 'myimage'
    diskName = 'mydisk'
    diskSizeGb = 30
    autoDelete = False
    ret_config = create_config_bootdisk_from_image(
        sourceImage, diskName, diskSizeGb, autoDelete,
        diskType=DiskType.SCRATCH,
        diskMode=DiskMode.READ_ONLY,
        diskInterface=DiskInerface.NVME,
    )

    expected_config = {
        'boot': True,
        'autoDelete': autoDelete,
        'diskType': DiskType.SCRATCH.value,
        'mode': DiskMode.READ_ONLY.value,
        'interface': DiskInerface.NVME.value,
        'initializeParams': {
            'sourceImage': sourceImage,
            'diskName': diskName,
            'diskSizeGb': diskSizeGb,
        }
    }

    assert ret_config == expected_config


def test_create_config_bootdisk_from_image_with_invalid_type_arguments():

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image(1, '1')
    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', 1)
    assert create_config_bootdisk_from_image('1', '1')

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', '1', '10')
    assert create_config_bootdisk_from_image('1', '1', 10)

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', '1', '10', 'True')
    assert create_config_bootdisk_from_image('1', '1', 10, True)

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', '1', '10', True,
                                          DiskMode.READ_ONLY)
    assert create_config_bootdisk_from_image('1', '1', 10, True,
                                             DiskType.PERSISTENT)

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', '1', '10', True,
                                          DiskType.PERSISTENT,
                                          DiskType.PERSISTENT
                                          )
    assert create_config_bootdisk_from_image('1', '1', 10, True,
                                             DiskType.PERSISTENT,
                                             DiskMode.READ_WRITE)

    with pytest.raises(AssertionError):
        create_config_bootdisk_from_image('1', '1', '10', True,
                                          DiskType.PERSISTENT,
                                          DiskMode.READ_WRITE,
                                          DiskMode.READ_WRITE
                                          )
    assert create_config_bootdisk_from_image('1', '1', 10, True,
                                             DiskType.PERSISTENT,
                                             DiskMode.READ_WRITE,
                                             DiskInerface.SCSI)
