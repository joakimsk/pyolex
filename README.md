# pyolex

Helper-scripts to work with Olex data, primarily Plotlayers (Ruter-file)

## Convert Decimal Degrees to Decimal Minutes (Olex-format)
Example code:
```
dd_coord = pyolex.DecimalDegreeCoord(61.6296187, 5.01738467)
min_coord = pyolex.decimal_degrees_to_decimal_minutes(dd_coord, precision=7)
print(min_coord.lat, min_coord.lon)
```
Output: 3697.777122 301.0430802

## Make a towline
Example code:
```
start_lat, start_lon = (61.6296187, 5.01738467)
stop_lat, stop_lon = (61.6396187, 5.01538467)

start_coord = pyolex.DecimalDegreeCoord(start_lat, start_lon)
stop_coord = pyolex.DecimalDegreeCoord(start_lat, start_lon)

towline = pyolex.TowlineObject(plotset=1,linecolor=pyolex.Color.RED, tow_start_dd=start_coord, tow_stop_dd=stop_coord)

print(towline)
```

Output:
```
Rute Slepestrek
Rutetype Strek
Linjefarge Rød
Plottsett 1
3697.777122 301.0430802 1675377136 Garnstart
3698.377122 300.9230802 1675377136 Garnstopp
```