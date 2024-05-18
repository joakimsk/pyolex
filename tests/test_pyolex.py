from pyolex import *

def test_pyolex_utilities_dd2dm():
    assert dd2dm(61.6296187, 5.01738467, precision=7) == (3697.777122, 301.0430802)
    assert dd2dm(61.6296187, 5.01738467, precision=4) != (3697.777122, 301.0431)
    assert dd2dm(61.6296187, 5.01738467, precision=4) == (3697.7771, 301.0431)

def test_pyolex_utilities_dm2dd():
    assert dm2dd(3697.777122, 301.0430802, precision=7) != (61.6296187, 5.01738467)
    assert dm2dd(3697.777122, 301.0430802, precision=7) == (61.6296187, 5.0173847)