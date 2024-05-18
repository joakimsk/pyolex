import datetime
import xml.etree.ElementTree as ET

import pyolex





dt_now = datetime.datetime.now()




tree = ET.parse('route_export_from_ecdis.rux')

root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)


waypoints = []

for elem in root.iter('WayPoint'):
    waypoints.append(pyolex.Waypoint(float(elem.attrib['Lat']), float(elem.attrib['Lon']), elem.attrib['WPName'], dt_now, pyolex.Symbol.BROWNCIRCLE))


olex_route = pyolex.generate_olex_route(waypoints, plotset=2, color=pyolex.Color.BLACK)
print()

f = open("output.olex", "w")
f.write(olex_route)
f.close()
