import pytest

from cloud_compute.gcp.gcp_instance_disk import *


def test_create_config_persistent_bootdisk_from_image_with_default_value():

    sourceImage = 'myimage'
    diskName = 'mydisk'
    ret_config = create_config_persistent_bootdisk_from_image(
        sourceImage, diskName
    )

    expected_config = {
        'boot': True,
        'autoDelete': True,
        'type': DiskLifeType.PERSISTENT.value,
        'mode': DiskMode.READ_WRITE.value,
        'interface': DiskInerface.SCSI.value,
        'initializeParams': {
            'sourceImage': sourceImage,
            'diskName': diskName,
            'diskSizeGb': 10,
            'DiskType': DiskType.PD_STANDARD.value
        }
    }

    assert ret_config == expected_config


def test_create_config_persistent_bootdisk_from_image_with_arguments():

    sourceImage = 'myimage'
    diskName = 'mydisk'
    diskSizeGb = 30
    autoDelete = False
    ret_config = create_config_persistent_bootdisk_from_image(
        sourceImage, diskName, diskSizeGb, autoDelete,
        diskType=DiskType.PD_SSD
    )

    expected_config = {
        'boot': True,
        'autoDelete': autoDelete,
        'type': DiskLifeType.PERSISTENT.value,
        'mode': DiskMode.READ_WRITE.value,
        'interface': DiskInerface.SCSI.value,
        'initializeParams': {
            'sourceImage': sourceImage,
            'diskName': diskName,
            'diskSizeGb': diskSizeGb,
            'DiskType': DiskType.PD_SSD.value
        }
    }

    assert ret_config == expected_config


def test_create_config_persistent_bootdisk_from_image_with_invalid_type_arguments():

    with pytest.raises(AssertionError):
        create_config_persistent_bootdisk_from_image(1, '1')
    with pytest.raises(AssertionError):
        create_config_persistent_bootdisk_from_image('1', 1)
    assert create_config_persistent_bootdisk_from_image('1', '1')

    with pytest.raises(AssertionError):
        create_config_persistent_bootdisk_from_image('1', '1', '10')
    assert create_config_persistent_bootdisk_from_image('1', '1', 10)

    with pytest.raises(AssertionError):
        create_config_persistent_bootdisk_from_image('1', '1', '10', 'True')
    assert create_config_persistent_bootdisk_from_image('1', '1', 10, True)

    with pytest.raises(AssertionError):
        create_config_persistent_bootdisk_from_image('1', '1', '10', True,
                                                     diskType=DiskInerface.SCSI)
    assert create_config_persistent_bootdisk_from_image('1', '1', 10, True,
                                                        diskType=DiskType.PD_STANDARD)
