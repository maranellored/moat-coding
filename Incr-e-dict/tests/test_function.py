from lib import function
from nose.tools import *

def test_basic():
    d = {}
    seq = ('a', 'b', 'c')
    function.incr_dict(d, seq)
    assert d['a']['b']['c'] == 1

    function.incr_dict(d, seq)
    assert d['a']['b']['c'] == 2

    function.incr_dict(d, seq)
    assert d['a']['b']['c'] == 3

def test_really_long_sequence():
    d = {}
    seq = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')
    assert len(d) == 0
    function.incr_dict(d, seq)

    assert len(d) == 1
    assert d['a']['b']['c']['d']['e']['f']['g']['h']['i']['j']['k']['l']['m']['n']['o']['p'] == 1

    function.incr_dict(d, seq)
    assert len(d) == 1
    assert d['a']['b']['c']['d']['e']['f']['g']['h']['i']['j']['k']['l']['m']['n']['o']['p'] == 2

def test_multiple_values():
    d = {}
    seq = ('a', 'b', 'c')
    assert len(d) == 0

    function.incr_dict(d, seq)
    assert len(d) == 1
    assert d['a']['b']['c'] == 1

    function.incr_dict(d, seq)
    assert len(d) == 1
    assert d['a']['b']['c'] == 2

    assert len(d['a']) == 1
    seq = ('a', 'r', 'f')
    function.incr_dict(d, seq)
    assert len(d['a']) == 2
    assert d['a']['r']['f'] == 1

    seq = ('a', 'z')
    assert len(d['a']) == 2
    function.incr_dict(d, seq)
    assert len(d['a']) == 3
    assert d['a']['z'] == 1

    function.incr_dict(d, seq)
    assert len(d['a']) == 3
    assert d['a']['z'] == 2

    assert d['a']['b']['c'] == 2

@raises(TypeError)
def test_replace():
    d = {}

    function.incr_dict(d, ('a'))
    assert d['a'] == 1
    function.incr_dict(d, ('a'))
    assert d['a'] == 2

    seq = ('a', 'b', 'c')
    function.incr_dict(d, seq)
