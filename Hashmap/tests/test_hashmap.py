from lib import hashmap
from nose.tools import *


def test_add():
    h = hashmap.HashMap()
    h.add('john', 'Google')
    assert h.get('john') == 'Google'


def test_negative_capacity():
    h = hashmap.HashMap(-10)
    assert h.size() == 0

    h.add('john', 'Google')
    assert h.get('john') == 'Google'


def test_add_with_resize():
    h = hashmap.HashMap(3)
    h.add('john', 'Google')
    h.add('jane', 'Amazon')
    h.add('victor', 12345)
    h.add('mark', 'Facebook')

    assert h.get('john') == 'Google'
    assert h.get('jane') == 'Amazon'
    assert h.get('mark') == 'Facebook'
    assert h.get('victor') == 12345


@raises(KeyError)
def test_remove():
    h = hashmap.HashMap()
    h.add('john', 'Google')
    assert h.size() == 1

    assert h.remove('john') == 'Google'
    assert h.size() == 0
    h.get('john')


@raises(KeyError)
def test_remove2():
    h = hashmap.HashMap(2)
    h.add('john', 'Google')

    h.remove('jim')

def test_get():
    h = hashmap.HashMap()

    h.add('john', 'Google')
    assert h.get('john') == 'Google'

    h.add('john', 'Facebook')
    assert h.get('john') == 'Facebook'
    assert not h.get('john') == 'Google'

@raises(KeyError)
def test_get_fail():
    h = hashmap.HashMap()
    h.get('john')


def test_size():
    h = hashmap.HashMap()

    assert h.size() == 0
    h.add('john', 'Google')
    h.add('jane', 'Amazon')
    h.add('victor', 12345)
    h.add('mark', 'Facebook')
    h.add('bill', 'Microsoft')
    h.add('elon', ('tesla', 'spacex'))
    assert h.size() == 6

    assert h.remove('elon') == ('tesla', 'spacex')
    assert h.remove('victor') == 12345
    assert h.size() == 4


def test_items():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, i)

    for k, v in h.items():
        assert k == v and k == list[k]


def test_keys():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, None)

    for key in h.keys():
        assert key == list[key]


def test_values():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, i)

    for value in h.values():
        assert value == list[value]


def test_iterkeys():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, i)

    for key in h.iterkeys():
        assert key == list[key]


def test_itervalues():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, i)

    for value in h.itervalues():
        assert value == list[value]


def test_iteritems():
    h = hashmap.HashMap()
    list = range(10)
    for i in list:
        h.add(i, i)

    for k, v in h.iteritems():
        assert k == v and k == list[k]
