import pyolex
import datetime

dt_now = datetime.datetime.now()

waypoints = [
    pyolex.Waypoint(59.52, 2.01552555, "", dt_now, pyolex.Symbol.BROWNCIRCLE),
    pyolex.Waypoint(59.22, 2.31552555, "StationS", dt_now,  pyolex.Symbol.BROWNCIRCLE)
]

olex_route = pyolex.generate_olex_route(waypoints, plotset=2, color=pyolex.Color.BROWN)
print(olex_route)
