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
