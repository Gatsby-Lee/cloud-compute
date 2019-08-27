"""
:author: Gatsby Lee
:since: 2019-08-25
"""

import pytest

from cloud_compute.gcp.gce import Metadatas


def test_init():
    Metadatas()


def test_init_with_kwargs():
    # test kwargs
    m = Metadatas(name='mlee', env='prod')
    assert m.get() == [{'key': 'name', 'value': 'mlee'}, {'key': 'env', 'value': 'prod'}]


def test_add():
    # test add key
    m = Metadatas()
    m.add('env', 'prod')
    assert m.get() == [{'key': 'env', 'value': 'prod'}]


def test_add_2():
    # test add key - overwrite exsting key
    m = Metadatas()
    m.add('env', 'prod')
    m.add('env', 'staging')
    assert m.get() == [{'key': 'env', 'value': 'staging'}]


def test_remove_key():
    # test remove key
    m = Metadatas(name='mlee', env='prod')
    m.remove('name')
    assert m.get() == [{'key': 'env', 'value': 'prod'}]


def test_enable_oslogin():
    # test remove key
    m = Metadatas()
    m.enable_oslogin()
    assert m.get() == [{'key': 'enable-oslogin', 'value': 'TRUE'}]


def test_disable_oslogin():
    # test remove key
    m = Metadatas()
    m.disable_oslogin()
    assert m.get() == [{'key': 'enable-oslogin', 'value': 'FALSE'}]


def test_remove_key_exception():
    # test remove key
    m = Metadatas(name='mlee', env='prod')
    with pytest.raises(KeyError):
        m.remove('mlee')
