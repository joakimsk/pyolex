#!/usr/bin/env python

# Make Olex objects - Joakim Skjefstad

import time
from typing import NamedTuple

class DecimalDegreeCoordinate(NamedTuple):
    lat: float
    lon: float

class DecimalMinuteCoordinate(NamedTuple):
    lat: float
    lon: float

def decimal_degrees_to_decimal_minutes(DecimalDegreeCoordinate, precision=7):
    min_lat = DecimalDegreeCoordinate.lat*60
    min_lon = DecimalDegreeCoordinate.lon*60
    min_lat_rounded = round(min_lat, precision)
    min_lon_rounded = round(min_lon, precision)
    return DecimalMinuteCoordinate(min_lat_rounded, min_lon_rounded)

def decimal_minutes_to_decimal_degrees(DecimalMinuteCoordinate, precision=7):
    dd_lat = DecimalMinuteCoordinate.lat/60
    dd_lon = DecimalMinuteCoordinate.lon/60
    dd_lat_rounded = round(dd_lat, precision)
    dd_lon_rounded = round(dd_lon, precision)
    return DecimalDegreeCoordinate(dd_lat_rounded, dd_lon_rounded)

class Waypoint:
    def __init__(self, lat, lon, precision=7, creation_time=time.time(), symbol="Brunsirkel"):
        self.dd_lat = lat
        self.dd_lon = lon

        self.dd_coord = DecimalDegreeCoordinate(lat, lon)
        self.display_precision = precision
        self.min_coord = decimal_degrees_to_decimal_minutes(self.dd_coord, self.display_precision)
        self.creation_time = int(creation_time)
        self.symbol = symbol
    
    def __str__(self):
        s_min_lat = f"{self.min_coord.lat:.{self.display_precision}f}"
        s_min_lon = f"{self.min_coord.lon:.{self.display_precision}f}"
        s_creation_time = str(self.creation_time)
        final_line = ' '.join([s_min_lat, s_min_lon, s_creation_time])
        return final_line


class PlotlayerObject:
    def __init__(self, plottsett):
        self.plottsett = plottsett


def main():
    dd_lat = 61.6296186667
    dd_lon = 5.01738466667
    
    min_object = decimal_degrees_to_decimal_minutes(DecimalDegreeCoordinate(dd_lat, dd_lon))
    dd_object = decimal_minutes_to_decimal_degrees(DecimalMinuteCoordinate(min_object.lat, min_object.lon))
    
    print(dd_lat, dd_lon)
    print(min_object.lat, min_object.lon)
    print(dd_object.lat,dd_object.lon)

    awaypoint = Waypoint(dd_lat, dd_lon)
    print(awaypoint)

if __name__=='__main__':
    main()