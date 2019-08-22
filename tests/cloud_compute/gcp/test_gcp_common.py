import pytest


def test_tag():
    from cloud_compute.gcp import Tags

    # basic test
    t = Tags()
    t.add('abc')
    assert t.get() == ['abc']

    # basic test - no duplication
    t = Tags()
    t.add('abc')
    t.add('abc')
    assert t.get() == ['abc']

    # basic get test
    t = Tags('abc', 'cde')
    assert sorted(t.get()) == ['abc', 'cde']

    # basic remove test
    t = Tags('abc', 'cde')
    t.remove('cde')
    assert sorted(t.get()) == ['abc']
    # test exception when removing non-existing tag
    with pytest.raises(KeyError):
        t.remove('cde')


def test_metadata():
    from cloud_compute.gcp import Metadatas

    # test kwargs
    m = Metadatas(name='mlee', env='prod')
    assert m.get() == [{'key': 'name', 'value': 'mlee'}, {'key': 'env', 'value': 'prod'}]

    # test remove key
    m = Metadatas(name='mlee', env='prod')
    m.remove('name')
    assert m.get() == [{'key': 'env', 'value': 'prod'}]

    # test - modifying existing key's value
    m = Metadatas(name='mlee', env='prod')
    m.add('name', 'mlee2')
    assert m.get() == [{'key': 'name', 'value': 'mlee2'}, {'key': 'env', 'value': 'prod'}]
