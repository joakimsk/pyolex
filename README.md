### pyolex

A python library for writing [Olex](https://olex.no/) plotlayer ("Ruter") files including utility functions for converting decimal degrees to decimal minutes. Reading is planned implemented in the future.

[![License][license-image]][license-url]

##### Installation from pypi

```bash
pip3 install pyolex
```

###### Dependencies
The project has no major dependencies. Some examples may require more advanced dependencies like pandas.

##### Usage
###### Convert Decimal Degrees to Decimal Minutes (Olex-format)
Example code:
```
import pyolex

dd_coord = pyolex.DecimalDegreeCoord(61.6296187, 5.01738467)
min_coord = pyolex.decimal_degrees_to_decimal_minutes(dd_coord, precision=7)
print(min_coord.lat, min_coord.lon)
```
Output: 3697.777122 301.0430802

###### Make a towline
Example code:
```
import pyolex

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

##### Contribution
If you are missing functionality or find bugs, either submit a patch, or be prepared to send example "Ruter"-file when submitting the bug-report.

### License
pyolex is open-source and licensed under GNU GPL, Version 3.

<!-- Badges -->
[license-image]: https://img.shields.io/github/license/joakimsk/pyolex.svg?color=blue
[license-url]: https://github.com/joakimsk/pyolex/blob/main/LICENSE.md