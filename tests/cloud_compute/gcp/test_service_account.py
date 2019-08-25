import pytest

from cloud_compute.gcp import ServiceAccounts


def test_init():
    ServiceAccounts()


def test_default_init():
    s = ServiceAccounts()
    assert s.get() == []


def test_create_default():
    s = ServiceAccounts.create_default()
    config = s.get()
    expected_config = [{'email': 'default', 'scopes': [
        'https://www.googleapis.com/auth/devstorage.read_only',
        'https://www.googleapis.com/auth/logging.write',
        'https://www.googleapis.com/auth/monitoring.write',
        'https://www.googleapis.com/auth/pubsub',
        'https://www.googleapis.com/auth/service.management.readonly',
        'https://www.googleapis.com/auth/servicecontrol',
        'https://www.googleapis.com/auth/trace.append'
    ]}]
    assert len(config) == len(expected_config)
    assert len(config[0]['email']) == len(expected_config[0]['email'])
    assert set(config[0]['scopes']) == set(expected_config[0]['scopes'])


def test_add():
    s = ServiceAccounts()
    s.add('default', 'https://www.googleapis.com/auth/logging.write')
    config = s.get()
    expected_config = [{'email': 'default', 'scopes': [
        'https://www.googleapis.com/auth/logging.write',
    ]}]
    assert len(config) == len(expected_config)
    assert len(config[0]['email']) == len(expected_config[0]['email'])
    assert set(config[0]['scopes']) == set(expected_config[0]['scopes'])


def test_remove_scope():
    s = ServiceAccounts()
    s.add('default',
          'https://www.googleapis.com/auth/logging.write',
          'https://www.googleapis.com/auth/pubsub')
    s.remove_scope('default', 'https://www.googleapis.com/auth/pubsub')
    config = s.get()
    expected_config = [{'email': 'default', 'scopes': [
        'https://www.googleapis.com/auth/logging.write',
    ]}]
    assert len(config) == len(expected_config)
    assert len(config[0]['email']) == len(expected_config[0]['email'])
    assert set(config[0]['scopes']) == set(expected_config[0]['scopes'])


def test_remove_email():
    s = ServiceAccounts()
    s.add('default',
          'https://www.googleapis.com/auth/logging.write',
          'https://www.googleapis.com/auth/pubsub')
    s.remove_email('default')
    config = s.get()
    expected_config = []
    assert len(config) == len(expected_config)


def test_remove_email_exception():
    s = ServiceAccounts()
    with pytest.raises(KeyError):
        s.remove_email('default')


def test_remove_scope_exception():
    s = ServiceAccounts()
    s.add('default', 'https://www.googleapis.com/auth/logging.write')
    with pytest.raises(KeyError):
        s.remove_scope('default', 'https://www.googleapis.com/auth/pubsub')


def test_add_more_than_one_email_exception():
    s = ServiceAccounts()
    s.add('default',
          'https://www.googleapis.com/auth/logging.write')
    with pytest.raises(ValueError):
        s.add('other-service-account',
              'https://www.googleapis.com/auth/logging.write')
