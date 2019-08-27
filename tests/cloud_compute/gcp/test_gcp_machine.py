import pytest


def test_machine_type_init():
    from cloud_compute.gcp.gce.gce_machine import MachineType
    m = MachineType('us-east1-a', 'n1-standard-1')
    assert m.get() == 'zones/us-east1-a/machineTypes/n1-standard-1'


def test_machine_type_custom_memory_exception():
    from cloud_compute.gcp.gce.gce_machine import MachineType
    with pytest.raises(ValueError):
        MachineType('us-east1-a', 'custom-8-1023')
