def dd2dm(dd_lat, dd_lon, precision=7):
    # Check input validity
    if -90 < dd_lat < 90:
        pass
    else:
        raise ValueError('DD Lat invalid, must be between -90 and 90. It was', dd_lat)

    if -180 < dd_lon < 180:
        pass
    else:
        raise ValueError('DD Lon invalid, must be between -180 and 180. It was', dd_lon)

    dm_lat = dd_lat*60
    dm_lon = dd_lon*60
    dm_lat_rounded = round(dm_lat, precision)
    dm_lon_rounded = round(dm_lon, precision)
    return dm_lat_rounded, dm_lon_rounded

def dm2dd(dm_lat, dm_lon, precision=7):
    # Check input validity
    if -5400 < dm_lat < 5400:
        pass
    else:
        raise ValueError('MIN Lat invalid, must be between -5400 and 5400. It was', dm_lat)

    # Check input validity
    if -10800 < dm_lon < 10800:
        pass
    else:
        raise ValueError('MIN Lon invalid, must be between -10800 and 10800. It was', dm_lon)

    dd_lat = dm_lat/60
    dd_lon = dm_lon/60
    dd_lat_rounded = round(dd_lat, precision)
    dd_lon_rounded = round(dd_lon, precision)
    return dd_lat_rounded, dd_lon_rounded