from pyolex import *

def test_pyolex_utilities_decimal_degrees_to_decimal_minutes():
    assert decimal_degrees_to_decimal_minutes(DecimalDegreeCoord(61.6296187, 5.01738467)) == DecimalMinuteCoord(lat=3697.777122, lon=301.0430802)